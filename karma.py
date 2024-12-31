import random

# ========================================
# CONFIGURATION AND HELPER STRUCTURES
# ========================================

RANK_ORDER = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# Build a dictionary to compare ranks by index
RANK_VALUE = {rank: i for i, rank in enumerate(RANK_ORDER)}

def get_rank(card: str) -> str:
    """
    Return just the rank portion, e.g. '10' from '10H', or '7' from '7S'.
    """
    if card.startswith('10'):
        return '10'
    return card[:-1]

def top_effective_rank(discard_pile):
    """
    Determine the rank that matters for ascending-order checks.
    - Ignore 8s on top (they're 'invisible').
    - If the pile is empty, treat top rank as '2' (lowest).
    """
    if not discard_pile:
        return '2'  # If there's no card, treat baseline as '2' (lowest)
    
    # Scan from top down for the first non-8 card
    for card in reversed(discard_pile):
        rank = get_rank(card)
        if rank != '8':
            return rank
    # If the entire pile is 8s, effectively treat as '2'
    return '2'

def can_play(current_rank, test_rank, nine_as_higher=True):
    """
    Check if test_rank is >= current_rank in ascending order,
    considering the special '9' behavior (which can act higher or lower).
    """
    # If it's '2', always allowed (but the effect sets the next rank to '2' afterward)
    if test_rank == '2':
        return True

    # 8 is invisible, also always allowed for now
    if test_rank == '8':
        return True

    # 9 can be chosen to act as higher or lower
    if test_rank == '9':
        if nine_as_higher:
            return RANK_VALUE['9'] >= RANK_VALUE[current_rank]
        else:
            return RANK_VALUE['9'] <= RANK_VALUE[current_rank]

    # Otherwise, normal ascending check
    return RANK_VALUE[test_rank] >= RANK_VALUE[current_rank]

def check_four_in_a_row(discard_pile):
    """
    If the top 4 cards of discard_pile have the same rank => True => burn.
    """
    if len(discard_pile) < 4:
        return False
    last_four = discard_pile[-4:]
    ranks = [get_rank(card) for card in last_four]
    return len(set(ranks)) == 1

# ========================================
# DEALING THE CARDS
# ========================================

def build_deck():
    suits = ['H','D','S','C']
    deck = [rank + suit for rank in RANK_ORDER for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players):
    """
    Each player:
      - 3 face-down
      - 3 face-up
      - 3 in-hand
    Return:
      players = {
        'Player 1': {
           'hand': [...],
           'face_up': [...],
           'face_down': [...]
        },
        'Player 2': {...},
        ...
      }
    and the leftover deck (unused) if any.
    """
    players = {}
    cards_needed_per_player = 9  # 3 down + 3 up + 3 hand
    total_needed = cards_needed_per_player * num_players
    
    if total_needed > len(deck):
        raise ValueError("Not enough cards to deal with the requested number of players!")
    
    for i in range(num_players):
        pname = f"Player {i+1}"
        face_down = deck[:3]
        deck = deck[3:]
        
        face_up = deck[:3]
        deck = deck[3:]
        
        hand = deck[:3]
        deck = deck[3:]

        players[pname] = {
            "face_down": face_down,
            "face_up": face_up,
            "hand": hand
        }
    
    return players, deck  # leftover is the draw pile (if you want one)

# ========================================
# ZONE LOGIC (HAND -> FACE UP -> FACE DOWN)
# ========================================

def get_current_zone(players, pname):
    """
    Determine which zone the player should be playing from:
    1) 'hand' if not empty
    2) 'face_up' if hand is empty, face_up not empty
    3) 'face_down' if both hand + face_up are empty
    """
    if players[pname]["hand"]:
        return "hand"
    elif players[pname]["face_up"]:
        return "face_up"
    else:
        return "face_down"

# ========================================
# MAIN GAME LOGIC
# ========================================

def main_game():
    print("Welcome, Matt, to the ascending-order card game with face-down/up mechanics and magic cards!")
    num_players = int(input("How many players? (2-6) "))

    # Build and deal
    deck = build_deck()
    try:
        players, leftover = deal_cards(deck, num_players)
    except ValueError as e:
        print(e)
        return

    # For simplicity, let's store player names in a list for turn order
    turn_order = list(players.keys())
    current_idx = 0

    discard_pile = []
    
    # We track if the "top rank" is forced to '2' because of a '2' card
    # Actually, we can store that after a turn is played. If a 2 is played,
    # next time we read top_effective_rank, we'll see '2' anyway, so
    # we handle it simply in the effect function.

    while True:
        current_player = turn_order[current_idx]
        
        # If this player has no cards in all zones => they've won
        if (not players[current_player]["hand"] and
            not players[current_player]["face_up"] and
            not players[current_player]["face_down"]):
            print(f"\n{current_player} has no cards left! They win!")
            break
        
        print("\n========================================")
        print(f"It's {current_player}'s turn!")
        
        zone = get_current_zone(players, current_player)
        # Show partial info:
        if zone == "hand":
            print(f"Your HAND cards: {players[current_player]['hand']}")
        elif zone == "face_up":
            print(f"Your FACE-UP cards: {players[current_player]['face_up']}")
        else:
            # face_down
            # They can't see these, but let's just mention how many
            print(f"You have {len(players[current_player]['face_down'])} FACE-DOWN cards left (unknown!).")
        
        # Show top-of-pile rank
        effective_rank = top_effective_rank(discard_pile)
        if discard_pile:
            top_card = discard_pile[-1]
            print(f"Top of discard pile: {top_card} (effective rank: {effective_rank})")
        else:
            print("Discard pile is empty (treat top as '2').")
        
        # Let the user choose multiple cards if they're the same rank.
        # If zone == "face_down", we simulate flipping the top face-down card automatically.
        if zone == "face_down":
            facedown_cards = players[current_player]["face_down"]
            if not facedown_cards:
                print("No face-down cards to flip—strange, but skip turn.")
                # Move to next player
                current_idx = (current_idx + 1) % len(turn_order)
                continue
            
            # Flip the "top" face-down card (index 0 or last, your choice).
            card_flipped = facedown_cards.pop(0)
            print(f"You flip over: {card_flipped}")
            
            # Attempt to play it using the ascending/magic rules
            # Check if it's a 9 => ask high or low
            rank_flipped = get_rank(card_flipped)
            nine_as_higher = True
            if rank_flipped == '9':
                hi_lo = input("You've flipped a '9'. Play it as [H]igher or [L]ower? ").lower()
                if hi_lo.startswith('l'):
                    nine_as_higher = False
            
            if can_play(effective_rank, rank_flipped, nine_as_higher):
                discard_pile.append(card_flipped)
                print(f"Successfully played {card_flipped} on the pile!")
                
                # Check for burn or special effect
                burn, same_player_go_again = post_play_effects(
                    discard_pile, [card_flipped], current_player
                )
                
                if burn:
                    # Pile cleared
                    # same_player_go_again = True means we do NOT move to next player
                    if same_player_go_again:
                        print("You burned the pile and get to go again!")
                        continue
                else:
                    # Not burned
                    if same_player_go_again:
                        print("You get to go again!")
                        continue
                
                # Move on
                current_idx = (current_idx + 1) % len(turn_order)
            else:
                # Not valid => must pick up if there's anything to pick
                if discard_pile:
                    print("That card can't be played. You pick up the whole discard pile!")
                    players[current_player]["hand"].extend(discard_pile)
                    discard_pile.clear()
                else:
                    print("Discard pile empty, nothing to pick up. (Lucky!)")
                current_idx = (current_idx + 1) % len(turn_order)
            
            continue  # End face-down logic here
        
        else:
            # zone is either 'hand' or 'face_up'
            cards_in_zone = players[current_player][zone]
            if not cards_in_zone:
                # No cards to play here => skip
                print(f"No cards left in {zone} for {current_player}.")
                current_idx = (current_idx + 1) % len(turn_order)
                continue
            
            print(f"Cards available in {zone}: {cards_in_zone}")
            chosen_str = input(
                "Enter one or more cards of the SAME rank to play, space-separated.\n"
                "Or press ENTER if you cannot play (then you'll pick up the pile). "
            ).strip()
            
            if not chosen_str:
                # can't / won't play => pick up
                if discard_pile:
                    print("You can't play. You pick up the pile!")
                    players[current_player]["hand"].extend(discard_pile)
                    discard_pile.clear()
                else:
                    print("Pile is empty, nothing to pick up.")
                current_idx = (current_idx + 1) % len(turn_order)
                continue
            
            chosen_cards = chosen_str.split()
            # Validate
            if any(c not in cards_in_zone for c in chosen_cards):
                print("Invalid selection—at least one card isn't in your zone. You pick up the pile!")
                if discard_pile:
                    players[current_player]["hand"].extend(discard_pile)
                    discard_pile.clear()
                current_idx = (current_idx + 1) % len(turn_order)
                continue
            
            # Check all chosen cards are the same rank
            chosen_ranks = [get_rank(c) for c in chosen_cards]
            if len(set(chosen_ranks)) != 1:
                print("All chosen cards must share the SAME rank. You pick up the pile!")
                if discard_pile:
                    players[current_player]["hand"].extend(discard_pile)
                    discard_pile.clear()
                current_idx = (current_idx + 1) % len(turn_order)
                continue
            
            # Possibly handle '9' choice (high vs low)
            rank_chosen = chosen_ranks[0]
            nine_as_higher = True
            if rank_chosen == '9':
                hi_lo = input("You played '9'. Use it as [H]igher or [L]ower? ").lower()
                if hi_lo.startswith('l'):
                    nine_as_higher = False
            
            # Check if we can play the chosen rank vs top rank
            # We only need to compare once because they're all the same rank
            if not can_play(effective_rank, rank_chosen, nine_as_higher):
                # Must pick up
                print("Those cards can't be played (too low). You pick up the pile!")
                if discard_pile:
                    players[current_player]["hand"].extend(discard_pile)
                    discard_pile.clear()
                current_idx = (current_idx + 1) % len(turn_order)
                continue
            
            # Valid => remove them from player's zone and place on discard
            for c in chosen_cards:
                cards_in_zone.remove(c)
            discard_pile.extend(chosen_cards)
            
            print(f"{current_player} played {chosen_cards} on the discard pile.")
            
            # Post-play checks for 10, four-of-a-kind, etc.
            burn, same_player_go_again = post_play_effects(discard_pile, chosen_cards, current_player)
            
            if burn:
                # Pile is cleared
                if same_player_go_again:
                    print("Pile burned! You go again immediately!")
                    continue
                else:
                    print("Pile burned! Next player's turn.")
                    current_idx = (current_idx + 1) % len(turn_order)
            else:
                if same_player_go_again:
                    print("You get to go again!")  # This might not happen with current rules unless you want another effect
                    continue
                else:
                    current_idx = (current_idx + 1) % len(turn_order)

    print("\nGame over. Thanks for playing!")


def post_play_effects(discard_pile, just_played, player_name):
    """
    Applies the 'magic' rules:
      - If a 10 is played, burn the pile
      - If four of a kind (top 4 same rank), burn the pile
      - If a 2 is played, next compare rank is '2' automatically (handled by top_effective_rank logic)
      - If the pile is burned, the player goes again (don't move to next).
      - 9's effect is handled pre-check (the user chooses high/low).
      - 8 is invisible, so no direct effect besides skipping rank checks.

    Return: (burned: bool, same_player_go_again: bool)

    'same_player_go_again' is True if the pile gets burned by that player's action.
    """
    # Check for 10
    ranks_just_played = [get_rank(c) for c in just_played]
    if '10' in ranks_just_played:
        print("A '10' was played => burn the pile!")
        discard_pile.clear()
        return True, True  # pile burned, same player again

    # Check for four of a kind
    if check_four_in_a_row(discard_pile):
        print("Four-of-a-kind on top => burn the pile!")
        discard_pile.clear()
        return True, True
    
    # If no burn, return
    return False, False

# ========================================
# RUN
# ========================================

if __name__ == "__main__":
    main_game()
