class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def display(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')
        print()
        
    def enough(self, coffe_water, coffe_milk, coffee_beans):
        if self.water - coffe_water < 0:
            print('Sorry, not enough water!')
            print()
            return False
        elif self.milk - coffe_milk < 0:
            print('Sorry, not enough milk!')
            print()
            return False
        elif self.beans - coffee_beans < 0:
            print('Sorry, not enough coffee beans!')
            print()
            return False
        else:
            print('I have enough resources, making you a coffee!')
            print()
            return True
    
    def take(self):
        print('I gave you {self.money}')
        print()
        self.money = 0

    def fill(self):
        print('Write how many ml of water do you want to add:')
        added_water = int(input())
        self.water += added_water
        
        print('Write how many ml of milk do you want to add:')
        added_milk = int(input())
        self.milk += added_milk
        
        print('Write how many grams of coffee beans do you want to add:')
        added_beans = int(input())
        self.beans += added_beans
        
        print('Write how many disposable cups of coffee do you want to add:')
        added_cups = int(input())
        self.cups += added_cups

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        type = input()
        
        if type == '1':
            espresso_water = 250 
            espresso_beans = 16
            espresso_cost = 4
            
            if self.enough(espresso_water, 0, espresso_beans):
                self.water -= espresso_water
                self.beans -= espresso_beans
                self.cups -= 1
                self.money += espresso_cost
                
        elif type == '2':
            latte_water = 350 
            latte_milk = 75
            latte_beans = 20
            latte_cost = 7   
    
            if self.enough(latte_water, latte_milk, latte_beans):
                self.water -= latte_water
                self.milk -= latte_milk
                self.beans -= latte_beans
                self.cups -= 1
                self.money += latte_cost

        elif type == '3':
            cappuccino_water = 200
            cappuccino_milk = 100
            cappuccino_beans = 12
            cappuccino_cost = 6
            
            if self.enough(cappuccino_water,cappuccino_milk,cappuccino_beans):
                self.water -= cappuccino_water
                self.milk -= cappuccino_milk
                self.beans -= cappuccino_beans
                self.cups -= 1
                self.money += cappuccino_cost
        elif type == 'back':
            return None


coffee_machine = CoffeeMachine()
while True: 
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()  
      
    if action == 'buy':
        coffee_machine.buy()
    elif action == 'fill':
        coffee_machine.fill()
    elif action == 'take':
        coffee_machine.take()
    elif action == 'remaining':
        coffee_machine.display()
    elif action == 'exit':
        break
    
    