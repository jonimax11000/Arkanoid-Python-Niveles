from src.ball import Ball
from src.brick import Brick

def check_collision(ball, brick):
    if ball.x < brick.x + brick.width and ball.x + ball.radius > brick.x and ball.y < brick.y + brick.height and ball.y + ball.radius > brick.y:
        brick.destroy()
        return True
    return False

def check_collision_paddle(ball, paddle):
    if ball.x < paddle.x + paddle.width and ball.x + ball.radius > paddle.x and ball.y < paddle.y + paddle.height and ball.y + ball.radius > paddle.y:
        ball.bounce('up')
        return True
    return False