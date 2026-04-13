# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

VibeFinder is a music recommender which suggests music to people and is fully context-based. It analyzes a person's favorite music genre, mood, and energy level and recommends music based on that data. VibeFinder assumes that the listener knows what their genre and mood preferences are and can rate them on a scale of 0 to 1. This project is a simple simulation to display how real music recommenders work. 

---

## 3. How the Model Works  

VibeFinder observes three things for each song which are its mood, genre, and its energy level. Then, it compares that information with the data the user provided to it. The song gets a huge boost in score if the genre matches. However, if the mood matches, the score gets a smaller boost. For the energy category, the highest score occurs when the song's energy is closer to what the user wants. All of the three scores are then add together and the songs are ranked from highest to lowest. In the end, the top five songs are recommended.  

---

## 4. Data  

The catalog consists of 18 songs which include various different genres such as rock, lofi, pop, metal, EDM, soul, bossa nova, chiptune, R&B, folk, jazz, synthwave, ambient, and indie pop. The song moods include happy, chill, intense, relaxed, moody, focussed, and energetic. The dataset was expanded to 18 songs from originally 10 songs. The dataset is still very small though and so it doesn't represent the full diversity of one's musical taste. For example, the dataset still lacks many music genres such as country, classical, hip-hop songs, and many more. 

---

## 5. Strengths  

The system works very well for users that have super clear and common preferences when it comes to their favorite genres or moods. The top result almost always feels accurate when the user's mood and genre are both in the catalog. An instance which stood out to me was when the High-Energy Pop profile properly matched with Sunrise City as the top recommendation. Songs that keep ranking higher are those which feel energetically close to the user's target. This shows that the energy proximity scoring also functions really well.  

---

## 6. Limitations and Bias 

The genre category is highly over-prioritized as it carries twice the weight of mood. In other words, an amazing song in the incorrect genre will mostly always rank below a less fit song in the correct genre. Furthermore, the dataset is very small, so the same song repeatedly gets recommended across various profiles. Also, the mood field is stored as plain text, so moods such as "chill" and "relaxed" which are clearly very similar moods, get treated as completely different terms. Lastly, if the mood preference of a user isn't included in the dataset, the system doesn't even take that mood into consideration. It then only ranks by energy and ignores mood, which can lead to skewed results. 

---

## 7. Evaluation  

Four user profiles were tested by me: High-Energy Pop, Chill Lofi, Deep Intense, Rock, and a conflicting profile (EDM + sad + high energy). The first three profiles displayed accurate results which matched well. The conflicting profile showed a small error, this is due to the fact that tno song has a "sad" mood. Thus, the system fully skipped that mood entirely and used only the energy category. Furthermore, I attempted to cut the genre points in half and double the energy points. This led to the higher energy points ranking higher even though the genre was not a match. This displayed the true importance of point values and how much they affect the final outcomes. 


---

## 8. Future Work  

- Let users set their own weights instead of using fixed ones
- Put more songs in dataset so the same songs don't keep popping up
- Instead of text labels for mood values, use numerical values, so similar models score nearer to one another
- Add tempo proximity and valence to scoring function
- Add filter for diversity so the same artist doesn't reappear multiple times in the top results
---

## 9. Personal Reflection  

Creating this music recommender taught me that even though everything seems so simple, the logic behind everything is much more complicated than previously assumed. For example, not knowing how much weight to give each feature. The most shocking thing to see for me was if no song in the dataset matched the users preferences, instead of notifying the user, the system just ignored that preference. Platforms such as Spotify and Apple Music don't have this problem nearly as bad as the system I built. I definitely had a mindset shift on how music recommender platforms actually operate during the making of this project. Recommendations that feel like magic when they pop up at the top, are really just simple math and scorings that are weighted. 
