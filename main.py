def padel_cort_cost (court_type):
    if court_type== ("indoor"):
       return 30 
    elif court_type==("outdoor"):
        return 20 
    
def racket_cost (racket_brand):
    if racket_brand=="bullpadel":
        return 100
    elif racket_brand=="nox":
        return 140 
    elif racket_brand=="siux":
        return 200

def padel_balls_cost(ball_boxes):
    if ball_boxes==1:
        return 2 
    elif ball_boxes==2: 
        return 3.5
    elif ball_boxes==3: 
        return 5 
    
def padel_game_cost():
    court_type= input("enter a court type: ").lower()
    racket_brand= input("enter your racket brand of choice :").lower()
    ball_boxes=int(input("enter the number of ball boxes: "))
    return racket_cost(racket_brand)+ padel_balls_cost(ball_boxes)+ padel_cort_cost(court_type)

game= padel_game_cost()
print(game)
