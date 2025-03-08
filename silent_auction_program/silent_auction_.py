import os

def find_winner(bidder_details):# { Akhil:1000,ram:30000,tom:45555}
    greatest_bid=0
    winner=""
    for bidder in bidder_details: #Akhil
        bidder_price=bidder_details[bidder]#fetching
        if bidder_price>greatest_bid:
            greatest_bid=bidder_price
            winner=bidder
    print(f"Here is the bidders: {bidder_details}")
    print(f"The winner is {winner} with a bid price of {greatest_bid}")
        
bidder_data={}

end_of_bidding=False
while not end_of_bidding:
    


    name=input("what is your name ?")
    price=int(input("what is your bid price?"))



    bidder_data[name]=price

    more_bidders=input("if there is bidders type 'yes or if no bidders type 'no'").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')#for clearing if we are working in windows


