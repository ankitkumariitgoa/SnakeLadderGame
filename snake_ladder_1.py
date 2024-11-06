import streamlit as st
import matplotlib.pyplot as plt
import random
import time
from PIL import Image
def run():
    # st.set_page_config(layout='wide')
    st.write("""    
    # :orange[Snakes and Ladder Game]🐍🪜🎲
    """)
    st.markdown("""
    # :orange[Welcome To Player vs Player Mode]""")
    c1, c2 = st.columns(2)
    p1 = c1.text_input('Player 1 Name:', placeholder='Type name here..')
    p2 = c2.text_input('Player 2 Name', placeholder='Type name here..')
    if p1 and p2:
        clr1 = c1.selectbox("Select Player 1's color", ['red', 'blue', 'green', 'orange','grey','violet'])
        clr2 = c2.selectbox("Select Player 2's color", ['blue', 'red', 'green', 'orange','grey','violet'])

        #splitting screen into two columns d1 and d2
        d1, d2 = st.columns(2)

        # Assigning variables for player1_position , player2_Position,and turn
        if "player1_position" not in st.session_state:
            st.session_state.player1_position =0
        if "player2_position" not in st.session_state:
            st.session_state.player2_position =0
        if "turn" not in st.session_state:
            st.session_state.turn = 1
            
        #Coordinates of snake and ladder 
        snake = {(16,6), (49, 11), (62, 19), (93, 90), (95, 61), (98, 78), (50,66)}
        ladder = {(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (51, 67), (71, 92), (80, 99)}
        org_snake_pos = {96:85,90:59,82:32,31:6,60:36,31:6,23:3,20:8}
        org_ladder_pos = {2:21,9:30,14:78,37:50,52:71,63:91,70:99,87:94}
        snakes = {i[0]: i[1] for i in snake}
        ladders = {j[0]: j[1] for j in ladder}

        #assigning variable for dice roll for both players
        a = 0 #for player 1
        b = 0 #for player 2

        #Drawing board
        def draw_board(player1_position, player2_position):
            fig, ax = plt.subplots(figsize=(14,14))
            for row in range(10):
                for col in range(10):
                    cell_num = (9 - row) * 10 + col + 1 if row % 2 == 0 else (9 - row) * 10 + (9 - col) + 1
                    if cell_num == player1_position and cell_num == player2_position:
                        color = 'purple'  
                    elif cell_num == player1_position:
                        color = clr1
                    elif cell_num == player2_position:
                        color = clr2
                    else:
                        color = 'white'
                    ax.text(col + 0.5, 9 - row + 0.5, str(cell_num), va='center', ha='center',
                            bbox=dict(facecolor=color, edgecolor='black', boxstyle='round,pad=1'), fontsize=15)
            for i in range(11):
                ax.axhline(i,color='black')
                ax.axvline(i,color='black')

            #Drawing snakes
            for start, end in snakes.items():
                start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
                end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
                ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'r', linewidth=20, alpha=0.4)
            
            #Drawing ladders
            for start, end in ladders.items():
                start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
                end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
                ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'g', linewidth=20, alpha=0.4)
            
            ax.axis('off')
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            return fig

        # function for changing player's position
        def move_player(position, roll):
            if position + roll <= 100:
                new_position = position + roll
                if new_position in org_snake_pos.keys():
                    new_position = org_snake_pos[new_position]
                elif new_position in org_ladder_pos.keys():
                    new_position = org_ladder_pos[new_position]
                return new_position
            return position

        #inside d1
        with d1:
            #splitting d1 into four columns
            col1, col2, col3, col4 = st.columns(4)
            
            #inside col2
            with col2:
                st.write(f"#### :{clr1}[{p1}]")
                placeholder1=st.empty()
                default_image = Image.open("def.jpeg")
                placeholder1.image(default_image, use_column_width=True)
                uploaded_file = st.file_uploader("select the image for player 1")
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    placeholder1.image(image, use_column_width=True)
                else:
                    placeholder1.image(default_image, use_column_width=True)

                #creating button for player1's move
                button1 = st.button(f"{p1}'s Move")
                if button1 and st.session_state.turn == 1:
                    roll = random.randint(1, 6)
                    a = roll
                    
                    #Creating a list containing the path of images of different faces of dice
                    image=["face_1.png","face_2.png","face_3.png","face_4.png","face_5.png","face_6.png"]
                    lst=[]
                    for i in range(5):
                        #Shuffling the image list and adding it to lst
                        random.shuffle(image)
                        lst=lst+image
                        
                    #creating an empty space for placing an image of dice faces further
                    placeholder = st.empty()
                    
                    #Displaying images at the empty spaces randomly
                    if True:
                        for image_path in lst:
                            img = Image.open(image_path)
                            placeholder.image(img)
                            time.sleep(0.1)
                    
                    #placing the final image
                    placeholder.image(f"face_{roll}.png")    
                    
                    #Assigning new position to player 1 after the roll of dice
                    st.session_state.player1_position = move_player(st.session_state.player1_position, roll)
                    
                    #Changing the turn to player 2
                    st.session_state.turn = 2
                    
                    # Winning condition for player 1
                    if st.session_state.player1_position == 100:
                        st.balloons()
                        st.write(f"🎉 Congratulations! {p1} wins!")
                    elif move_player(st.session_state.player1_position,roll) == st.session_state.player1_position:
                        st.write("Roll Exceeded 🙂!! Try Again")
                    
                
            #inside col3
            with col3:
                st.markdown(f"#### :{clr2}[{p2}]")
                placeholder2=st.empty()
                default_image = Image.open("def.jpeg")
                placeholder2.image(default_image, use_column_width=True)
                uploaded_file = st.file_uploader("select the image for player 2")
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    placeholder2.image(image, use_column_width=True)
                else:
                    placeholder2.image(default_image, use_column_width=True)

                #same logic as above for player 2
                
                
                button2 = st.button(f"{p2}'s "" Move")
                
                if button2 and st.session_state.turn == 2:
                    roll = random.randint(1, 6)
                    b = roll
                    image=["face_1.png","face_2.png","face_3.png","face_4.png","face_5.png","face_6.png",]
                    lst=[]
                    for i in range(random.randint(1,4)):
                        random.shuffle(image)
                        lst=lst+image
                    placeholder = st.empty()
                    if True:
                        for image_path in lst:
                            img = Image.open(image_path)
                            placeholder.image(img)
                            time.sleep(0.1)
                    placeholder.image(f"face_{roll}.png")
                    
                    st.session_state.player2_position = move_player(st.session_state.player2_position, roll)
                    st.session_state.turn = 1
                    
                    if st.session_state.player2_position == 100:
                        st.balloons()
                        st.write(f"🎉 Congratulations! {p2} wins!")

                    elif move_player(st.session_state.player2_position,roll) == st.session_state.player2_position:
                        st.write("Roll Exceeded 🙂!! Try Again")

        # To play again if any player wins 
        if st.session_state.player1_position==100 or st.session_state.player2_position==100:
            st.markdown("""
            ### :blue[Play Again..]""")
            
            #creating reload button to play again
            reload_button = st.button("Play Again")
            
            if reload_button:
                st.session_state.player2_position = 0
                st.session_state.player1_position = 0
                
        #Marking players move and their current position
        st.markdown(f""" 
        # :{clr1}[{p1}'s Move ->] {a}""")
        st.markdown(f"""
        # :{clr1}[{p1}'s Position ->]  {st.session_state.player1_position}""")
        st.markdown(f"""
        # :{clr2}[{p2}'s  Move ->] {b}""")
        st.markdown(f"""
        # :{clr2}[{p2}'s Position ->] {st.session_state.player2_position}""")

        #Plotting bar graph representing their current position
        fig, ax = plt.subplots()
        positions = [st.session_state.player1_position, st.session_state.player2_position]
        ax.bar([f'{p1}', f'{p2}'], positions, color=[clr1, clr2])
        ax.set_title("Current Positions")
        st.pyplot(fig)

        #Showing player's turn 
        if st.session_state.turn == 1:
            with col1:
                st.markdown(f"""
            ### :{clr1}[{p1}'s Move]""")
        else:
            with col4:
                st.markdown(f"""
        ### :{clr2}[{p2}'s Move]""")

        #plotting bar graph in column d2
        with d2:
            st.pyplot(draw_board(st.session_state.player1_position, st.session_state.player2_position))
