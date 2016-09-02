# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

#Personagens principal e sacundarios
define A = Character('Aureus', color = "#FF8C00")
define colin = Character('Colin', color="#00ffff")
define M = Character('Meridien', color = "#228B22")

#Personagens figurantes
define waitress = Character('Waitress', color="#ADD8E6")
define guard = Character('Guard', color ="#A9A9A9")
define guard2 = Character('Guard2', color ="#A9A9A9")

#transições
define normalDissolve = Dissolve(2)

# The game starts here.
label start:
    
    scene black
    with normalDissolve
    
    "Alguma frase foda...{w}"

    "Que um personagem do jogo vai falar."
    
    scene Imagem de fundo
    with normalDissolve
    
    "It's been a while since I had a good night of sleep."
    
    "The spreading of the word of god is top priority to the Great Bishop now." 
    
    "Is the duty that our highness assigned us since the invasions that came from the east."
    
    "Some of us are sent to lands far away from the limits. In regions that, most of the times, the people disagree with us. A suicide mission if you want to now what I think."
    
    "But, as our Great Bishop says, it's for the sake of god."
    
    "And is our mission... MY mission, as a cleric, to be the hand of Rouhl over the world."
    
    "If this isn't enough, there are these dreams... They're driving me crazy! Strange images keep showing inside my head like a lot of bad memories."
    
    "They're so real, but I don't see any sense on them... What the hell is happening to me?"
    
    colin "Aureus!"
    
    colin "It's almost midnight."
    
    colin "We should rest in the local inn for the time being. These roads can be very dangerous at night."
    
    
    scene black
    with normalDissolve
    
    "The next morning..."
    
    scene sonho
    with normalDissolve
    pause(5)
    
    scene de volta na teverna
    with normalDissolve
    
    A "No!!!...."
    
    A "......"
    
    A "Another dream..."
    
    A "Colin, I hope you didn't tried to get laid with the waitress like in the last time."
    
    A "It's getting harder and harder to find an inn that you're not banished."
    
    A "Colin..."
    
    A "(Where the hell is this guy?)"
    
    scene black
    with normalDissolve
    pause(5)
    
    scene corredor
    with normalDissolve
    
    A "Why is it so crowded around here?"
    
    A "Excuse me, miss, do you know where is the man that came with me?"
    
    waitress "Sir, I think you should see this."
    
    A "See what?"
    
    waitress "It's your friend..."
    
    scene white
    with normalDissolve
    
    scene cara morto
    
    A "C-Colin!?"
    
    A "What happened?"
    
    waitress "We found him like that some minutes ago. We already called the guards."
    
    waitress "Looks like he killed himself in the middle of the night."
    
    A "(Killed himself? Why?)"
    
    guard "Stand aside!"
    
    guard2 "Looks like someone proved Mya's food again."
    
    waitress "Cut the crap Leal, this is serious."
    
    guard2 "Ok. It's just a joke, alright!?"
    
    guard2 "Alright everybody. Show's over. Go back to your doings."
    
    #passos
    pause(5)
    
    guard "Can I help You sir?"
    
    A "That guy was my friend. We were on the road to Red-Solis and stoped by to rest."
    
    guard2 "Red-Solis? Now I know why he did this..."
    
    guard "Shut up, idiot."
    
    guard "Sir, we checked the scene but it seems that it really was a suicide."
    
    guard "All we could find near the body was this piece of paper with estrange simbols."
    
    A "Let me have it."
    
    A "(This symbols... I'm sure that I've already seen them before.)"
    
    guard "Cases like these have been heppening since last week."
    
    guard "Some think that this is some kind of curse casted over this town by the heathens."
    
    guard "But we've been keeping our eyes peeled on the roads for people coming from that way."
    
    A "(What )"
    #caiu a criatividade aqui
    
    scene black
    with normalDissolve
    
    "3 hours later"
    
    scene lado de fora
    with normalDissolve
    
    A "(Something is missing in all this mess...)"
    
    A "(Why would Colin commit suicide? He hardly complained about anything.)"
    
    A "(And this note. They're kind of familiar to me.)"
    
    

# mDepois de encontrar o inspetor
#    A "(This symbols are from the language of the octo-flamina.)"
#    A "(I have a book about this language on my horse.)"
    
    
    return


