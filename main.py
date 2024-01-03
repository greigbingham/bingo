#number of simulations
run_count = 5000
#tracker for count of games going down to last three numbers
last_three_count = 0

#create three bingo cards and simlate the final three numbers
for _ in range(run_count):
    cards_15_1 = create_cards(15)
    cards_15_2 = create_cards(15)
    cards_15_3 = create_cards(15)
    card_3 = create_cards(3)

    #check for incomplete bingo cards in remaining three cards
    common_numbers = [len([1 for number in card if number in card_3]) for card in [cards_15_1, cards_15_2, cards_15_3]]
 
    if all(number == 1 for number in common_numbers):
        last_three_count += 1

#final printout
percentage = (last_three_count / run_count) * 100
print(f"Based on {run_count} simulations, the chance of three bingo players requiring one number each with three numbers left is: {percentage}%")
