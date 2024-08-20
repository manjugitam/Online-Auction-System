class Auction:
    def __init__(self, item_name, starting_bid):
        self.item_name = item_name
        self.starting_bid = starting_bid
        self.current_bid = starting_bid
        self.highest_bidder = None
        self.is_open = True

    def place_bid(self, bidder_name, bid_amount):
        if not self.is_open:
            return "Auction is closed."
        if bid_amount <= self.current_bid:
            return "Bid must be higher than the current bid."
        self.current_bid = bid_amount
        self.highest_bidder = bidder_name
        return f"New highest bid of ${bid_amount} by {bidder_name}."

    def close_auction(self):
        self.is_open = False
        if self.highest_bidder:
            return f"Auction won by {self.highest_bidder} with a bid of ${self.current_bid}."
        else:
            return "No bids were placed."

# Example usage
auction = Auction("Antique Vase", 100)

print(auction.place_bid("Alice", 120))
print(auction.place_bid("Bob", 150))
print(auction.place_bid("Alice", 140))  # This bid will be rejected

print(auction.close_auction())
