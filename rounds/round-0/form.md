# Violin teaching survey · round 0

**form version:** `62ae93c5f7aa` · **rater:** ☐ the violinist · ☐ the author (Siyuan)

Paper version: cards in a fixed order, tick one box per question.

We built a computer system that watches and listens to someone playing the violin and measures 27 different things. Each card below describes one of them in plain words. For each one, tell us two things: do violin teachers care about it, and could a student use the number? There are no right answers.

## The two questions

**Question 1.** Do violin teachers pay attention to this in lessons?

**Question 2.** If a practice app reported this to a student, could the student act on it?  
*We mean the number itself, not just the idea.*

## How to answer

- **1** definitely not
- **2** probably not
- **3** probably yes
- **4** definitely yes

---

### 1. Bow speed (with direction)
<sub>bow_speed</sub>  
**Warm-up card: answer it like any other.**

How fast the bow is moving, and whether it is a down-bow or an up-bow. Zero means the bow is still; above zero is a down-bow, below zero an up-bow. Teachers call this "bow speed" (Fischer, Flesch).

**Question 1.** Do violin teachers pay attention to bow speed in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported bow speed to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2. Bow-hand wrist turn (direction 3 of 3)
<sub>right_wrist_aa_z_dev_deg</sub>  
**Warm-up card: answer it like any other.**

One of three ways the bow-hand wrist can turn, in degrees, as a computer body model measures it, compared with the player's usual wrist position. The three directions belong to the model, not to a teacher's vocabulary. The nearest teacher phrase is a "bent wrist" (Rolland).

**Question 1.** Do violin teachers pay attention to the bow-hand wrist turn (direction 3 of 3) in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the bow-hand wrist turn (direction 3 of 3) to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 3. Where the bow touches the string, compared with the player's usual spot
<sub>contact_bridge_ratio_dev</sub>

Whether the bow is touching the string closer to the bridge or closer to the fingerboard than this player usually does. Zero is the usual spot; below zero is nearer the bridge, above zero nearer the fingerboard. Teachers call this spot the "soundpoint" (Fischer) or "contact point" (Flesch).

**Question 1.** Do violin teachers pay attention to where the bow touches the string, compared with the player's usual spot in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported where the bow touches the string, compared with the player's usual spot to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 4. Which part of the bow is on the string
<sub>hair_pos</sub>

Whether the player is using the bow near the frog, the middle, or the tip. Zero is the frog, 0.5 the middle, 1 the tip. Teachers talk about playing "at the frog" or "at the tip" and about "bow distribution".

**Question 1.** Do violin teachers pay attention to which part of the bow is on the string in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported which part of the bow is on the string to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 5. Is the bow on the string or lifted off?
<sub>hair_string_gap_ratio</sub>

How far the bow hair is from the string. Zero means the bow is on the string; bigger numbers mean it is lifted further off. Teachers speak of playing "on the string" or "off the string".

**Question 1.** Do violin teachers pay attention to whether the bow is on the string or lifted off in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported whether the bow is on the string or lifted off to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 6. Is the bow straight or crooked?
<sub>skew_deg</sub>

How far the bow is from a right angle to the strings, in degrees. Zero is a perfectly straight bow; bigger numbers mean more crooked. Teachers say "keep the bow straight" and diagnose a "crooked bow" (Hamann & Gillespie).

**Question 1.** Do violin teachers pay attention to how straight the bow is in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported how straight the bow is to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 7. Which string the bow is leaning toward
<sub>string_side_deg</sub>

The tilt of the bow around the strings, in degrees, which shows which string it is playing or moving toward. Smaller numbers lean toward the G string, larger toward the E string. Teachers talk about "string crossing" (Galamian, Rolland).

**Question 1.** Do violin teachers pay attention to which string the bow is leaning toward in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported which string the bow is leaning toward to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 8. Bow speed (with direction)
<sub>bow_speed</sub>

How fast the bow is moving, and whether it is a down-bow or an up-bow. Zero means the bow is still; above zero is a down-bow, below zero an up-bow. Teachers call this "bow speed" (Fischer, Flesch).

**Question 1.** Do violin teachers pay attention to bow speed in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported bow speed to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 9. Bow speed (without direction)
<sub>bow_speed_abs</sub>

How fast the bow is moving, whether it is a down-bow or an up-bow. Zero means the bow is still; 1 means a full bow in one second. Teachers call this "bow speed" (Fischer, Flesch).

**Question 1.** Do violin teachers pay attention to bow speed, ignoring direction in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported bow speed, ignoring direction to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 10. How quickly the bow speeds up or slows down
<sub>bow_accel</sub>

Whether the bow is speeding up, slowing down, or moving steadily during a stroke. Zero means a steady speed; bigger numbers mean a quicker change. Teachers speak of "speeding up or slowing down the bow within a stroke".

**Question 1.** Do violin teachers pay attention to how quickly the bow speeds up or slows down in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported how quickly the bow speeds up or slows down to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 11. Down-bow or up-bow
<sub>direction_sign</sub>

Whether the bow is moving as a down-bow or an up-bow. Plus one is a clear down-bow, minus one a clear up-bow, and near zero means stopped or turning around. Teachers simply say "down-bow" and "up-bow".

**Question 1.** Do violin teachers pay attention to whether the bow is going down or up in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported whether the bow is going down or up to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 12. How bent the bow-arm elbow is
<sub>right_elbow_flexion_deg</sub>

How much the right elbow is bent, in degrees, estimated from a computer model of the body. Zero is a straight arm; bigger numbers mean more bend. Teachers talk about the "elbow angle" of the bow arm and about "whole-arm strokes" (Rolland).

**Question 1.** Do violin teachers pay attention to how bent the bow-arm elbow is in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported how bent the bow-arm elbow is to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 13. Bow-hand wrist turn (direction 1 of 3)
<sub>right_wrist_aa_x_dev_deg</sub>

One of three ways the bow-hand wrist can turn, in degrees, as a computer body model measures it, compared with the player's usual wrist position. The three directions belong to the model, not to a teacher's vocabulary. The nearest teacher phrase is a "bent wrist" (Rolland).

**Question 1.** Do violin teachers pay attention to the bow-hand wrist turn (direction 1 of 3) in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the bow-hand wrist turn (direction 1 of 3) to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 14. Bow-hand wrist turn (direction 2 of 3)
<sub>right_wrist_aa_y_dev_deg</sub>

One of three ways the bow-hand wrist can turn, in degrees, as a computer body model measures it, compared with the player's usual wrist position. The three directions belong to the model, not to a teacher's vocabulary. The nearest teacher phrase is a "bent wrist" (Rolland).

**Question 1.** Do violin teachers pay attention to the bow-hand wrist turn (direction 2 of 3) in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the bow-hand wrist turn (direction 2 of 3) to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 15. Bow-hand wrist turn (direction 3 of 3)
<sub>right_wrist_aa_z_dev_deg</sub>

One of three ways the bow-hand wrist can turn, in degrees, as a computer body model measures it, compared with the player's usual wrist position. The three directions belong to the model, not to a teacher's vocabulary. The nearest teacher phrase is a "bent wrist" (Rolland).

**Question 1.** Do violin teachers pay attention to the bow-hand wrist turn (direction 3 of 3) in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the bow-hand wrist turn (direction 3 of 3) to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 16. Bow-arm shoulder position, compared with the player's usual
<sub>right_shoulder_rotation_dev_deg</sub>

How far the right shoulder has moved from this player's usual position, in degrees, for example when it is raised or hunched. Zero is the usual position; bigger numbers mean further from it. Teachers warn about a "raised shoulder" (Rolland).

**Question 1.** Do violin teachers pay attention to the bow-arm shoulder position in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the bow-arm shoulder position to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 17. Head tilt
<sub>neck_tilt_deg</sub>

How far the head is tilted from upright, in degrees, in any direction. Zero is upright; bigger numbers mean more tilt. Teachers talk about "head position".

**Question 1.** Do violin teachers pay attention to head tilt in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported head tilt to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 18. Posture: upright or slouched
<sub>spine_curvature_deg</sub>

How much the upper body is bent forward or sideways from upright, in degrees. Zero is upright; bigger numbers mean more bend. Teachers simply call this "posture" (Kreitman, Flesch) or "slouching".

**Question 1.** Do violin teachers pay attention to posture in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported posture to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 19. How high the violin is held
<sub>violin_hold_height_ratio</sub>

How high the violin sits compared with the player's hips: lower when the scroll droops, higher when the violin is held up. Bigger numbers mean the violin is held higher. Teachers warn about "scroll drooping" (Auer).

**Question 1.** Do violin teachers pay attention to how high the violin is held in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported how high the violin is held to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 20. In tune, sharp, or flat
<sub>pitch_dev_semi</sub>

How far the note played is from the note written in the music, in semitones. Zero is in tune; above zero is sharp, below zero is flat. Teachers call this "intonation" (Fischer, Galamian).

**Question 1.** Do violin teachers pay attention to whether a note is in tune, sharp or flat in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported whether a note is in tune, sharp or flat to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 21. Loudness
<sub>env_db</sub>

How loud the sound is from moment to moment, in decibels. Higher numbers are louder; very low numbers mean silence. Teachers talk about "dynamics" and "volume".

**Question 1.** Do violin teachers pay attention to loudness in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported loudness to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 22. How strongly each note starts
<sub>onset_strength</sub>

How clearly and strongly a new note begins: high for a crisp, accented start, low in the middle of a held note. Teachers talk about the "attack" of a note and about accented strokes such as martelé.

**Question 1.** Do violin teachers pay attention to how strongly each note starts in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported how strongly each note starts to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 23. The note being played
<sub>f0_midi</sub>

Which pitch the violin is sounding at each moment, tracked continuously, so vibrato and slides show too. Higher numbers are higher notes. Teachers talk about "the note you are playing" and its "intonation" (Galamian).

**Question 1.** Do violin teachers pay attention to the note being played in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the note being played to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 24. How clean and clear the tone is
<sub>f0_salience</sub>

How clearly a definite note can be heard: high for a clean, focused tone, low for scratchy, noisy or silent moments. Teachers speak of a "clean tone" or a "scratchy tone" (Hamann & Gillespie); Fischer says "it is impossible to scratch if the bow keeps moving".

**Question 1.** Do violin teachers pay attention to how clean and clear the tone is in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported how clean and clear the tone is to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 25. Played on a different string than the music suggests
<sub>string_disagreement</sub>

How likely it is that the player used a different string from the one the written music points to. Zero means the same string; 1 means clearly a different one. Teachers say "wrong string" or "play it on the A string".

**Question 1.** Do violin teachers pay attention to whether the player used a different string than the music suggests in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported whether the player used a different string than the music suggests to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 26. Left-hand position, compared with what the music suggests
<sub>position_dev_semi</sub>

Whether the left hand was higher or lower on the fingerboard than the position the music points to, in semitones. Zero is the expected position; above zero is higher, below zero lower. Teachers say "stay in third position" and teach "shifting" (Fischer, Ding Zhinuo).

**Question 1.** Do violin teachers pay attention to the left-hand position compared with what the music suggests in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the left-hand position compared with what the music suggests to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 27. The player's usual bow-contact spot
<sub>contact_bridge_ratio_neutral</sub>

Where on the string this player's bow usually sits during a recording, between the bridge and the fingerboard, as one number for the whole recording. Zero is at the bridge; bigger numbers are nearer the fingerboard. Teachers call this the "soundpoint" (Fischer) or "contact point" (Flesch).

**Question 1.** Do violin teachers pay attention to the player's usual bow-contact spot in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app reported the player's usual bow-contact spot to a student, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

