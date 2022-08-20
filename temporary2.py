import matplotlib.pyplot as plt
tickets = ["England", "Iraq", "Waterways", "France", "Iran", "Satellite", "Egypt", "Canada",
           "Germany", "Airways", "Switzerland", "Brazil", "Italy", "Japan",
           "USA", "Roadways", "Mexico", "Hong Kong", "Australia", "India",
           "Saudi Arabia", "Petroleum", "China", "Railways", "Malaysia", "Singapore"]
ticket_prices = [2500, 5000, 9500, 2500, 2500, 2000, 3200, 4000, 3500, 10500, 3500, 2500, 3500,
                  2500, 8500, 3500, 4000, 2000, 3300, 4500, 5500, 5500, 4500, 9500, 1500, 3000]
ticket_rent =  [700, 500, 1400, 300, 300, 500, 300, 400, 400, 1500, 700, 300, 200, 250, 1000, 800, 900
               , 200,400, 550, 600, 500, 450, 1500, 200, 300]
tickets_quo = []
counter = 0
for i in ticket_rent:
    i = (ticket_prices[counter]/i)*1000
    plt.plot(tickets, ticket_prices, marker= 'o')
    tickets_quo.append(i)
    counter += 1
plt.plot(tickets,tickets_quo)
plt.title("Ticket Prices in USD")
plt.xlabel("Tickets")
plt.ylabel("Ticket prices (USD)")
plt.legend(['ticket prices', 'no.of times * 1000'])
plt.tight_layout
plt.grid(True)
plt.show()