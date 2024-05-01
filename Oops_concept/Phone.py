class Phone:
      
      def set_color(self,color):
            self.color=color  
      def set_cost(self,cost):
            self.cost=cost 
      def show_color(self):
            print(self.color) 
      def show_cost(self):
            print(self.cost)  
      def make_call(self):
            print("let's make a phone call")
            
      def play_game(self):
            print("let's play a game")

p2=Phone()
p2.make_call()
p2.play_game()
p2.set_color('purple')
p2.set_cost(100000)
p2.show_color()
p2.show_cost()

            