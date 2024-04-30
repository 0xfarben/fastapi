from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
import oauth

router = APIRouter(
    prefix= "/posts", # + /id
    tags= ['Posts']
)

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db : Session = Depends(get_db),
              current_user : int = Depends(oauth.get_current_user),
              Limit : int = 10,
              Skip: int = 0,
              Search : Optional[str] = ""):
    # Limit = How many posts the user wants to see
    #Skip = how many posts to skip (do not wanna display the required posts)
    # {{URL}}posts?Limit=10
    #  "?xyzyxz" --->> is called Optional Parameters
    # {{URL}}posts?Limit=5
    print(f"User with Email who wants to view all the post = {current_user.email}")
    # posts = db.query(models.Post).all()
    posts = db.query(models.Post).filter(models.Post.title.contains(Search)).limit(Limit).offset(Skip).all()

    # By default SQLAlchmey -> peroforms inner Join
    #  1. Making Left outer join
    # results1 = db.query(models.Post).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
    # print(results1)

    # 2.adding Group by clause
    # results2 = db.query(models.Post).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)
    # print(results2)

    # 3. Adding count aggegrate function
    results3 = db.query(models.Post,
                        func.count(models.Vote.post_id).label("votes")).join(
                        models.Vote, models.Vote.post_id == models.Post.id, isouter=True
                        ).group_by(models.Post.id).filter(
                            models.Post.title.contains(Search)).limit(Limit).offset(Skip).all()
    # print(results3)
    # results3 => SELECT posts.id AS posts_id, posts.title AS posts_title, 
    # posts.content AS posts_content, posts.published AS posts_published, 
    # posts.created_at AS posts_created_at, posts.owner_id AS posts_owner_id, 
    # count(votes.post_id) AS votes
    # FROM posts LEFT OUTER JOIN votes 
    # ON votes.post_id = posts.id 
    # GROUP BY posts.id

    return results3

@router.get("/{id}", 
            response_model=schemas.PostOut)
def get_post(id : int, 
             db : Session = Depends(get_db),
             current_user : int = Depends(oauth.get_current_user)):
    
    print(f"User with Email who wants to view the post-no.{id} = {current_user.email}")
    # This below query is for viewing the current user created posts
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    results = db.query(models.Post,
                    func.count(models.Vote.post_id).label("votes")).join(
                    models.Vote, models.Vote.post_id == models.Post.id, 
                    isouter=True).group_by(models.Post.id).filter(
                    models.Post.id == id).first()
    if not results :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Post {id} was not found")
    # if post.owner_id != current_user.id :
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="Not authorized to perform requested action")
    return results

@router.post("/", 
             status_code = status.HTTP_201_CREATED, 
             response_model=schemas.Post)
def create_posts(post : schemas.PostCreate, 
                 db : Session = Depends(get_db),
                 current_user : int = Depends(oauth.get_current_user)):
    print(f"User with Email who created the post = {current_user.email}")
    # Before - Without FK Constraint
    # new_post = models.Post(**(dict(post)))
    # After - With FK Constraint
    new_post = models.Post(owner_id = current_user.id, **(dict(post)))
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.put("/{id}", 
            response_model=schemas.Post)
def update_posts(id : int, 
                 updated_post : schemas.PostCreate, 
                 db : Session = Depends(get_db),
                 current_user : int = Depends(oauth.get_current_user)):
    print(f"User with Email who updated the post = {current_user.email}")
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id = {id} doesn't exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail="Not authorized to perform requested action")
    
    post_query.update(dict(updated_post), synchronize_session=False)
    db.commit()
    return post_query.first()

@router.delete("/{id}", 
               status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, 
                db : Session = Depends(get_db),
                current_user : int = Depends(oauth.get_current_user)):
    
    print(f"User with Email who deleted the post = {current_user.email}")
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id = {id} doesn't exist")
    
    if post.owner_id != current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)