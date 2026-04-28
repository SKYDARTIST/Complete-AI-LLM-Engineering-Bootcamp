from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(

    id = 1,
    content = "This is the first comment",
    replies = [
        Comment(
            id = 2,
            content = "This is the second comment",
            replies = [
                Comment(
                    id = 3,
                    content = "This is the third comment",
                    replies = []
                )
            ]
        )
    ]
)

print(comment)