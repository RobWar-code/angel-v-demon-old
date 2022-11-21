# ANGEL V DEMON

A command-line adventure/memory game for a solo player.

## Contents
<ul style="list-style: none;">
    <li>Systems Tests
        <ul>
            <li>Game Start Texts</li>
            <li>Input Point Tests</li>
            <li>Random Branch Point Tests</li>
            <li>Playability Tests</li>
        </ul>
    </li>
</ul>

## Systems Tests
### Game Start Texts

* Introduction Text

* Instruction Text

### Input Point Tests
All input tests are performed on game 1 paragraph, player level 1.
The Inn references relate to points on the flow-chart in 
doc/project-analysis.txt

Items completed are marked with * and screen shots given where
appropriate.

I01 Continue from introduction

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

I02 Continue from instructions

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. Check that the logic flows correctly from the inputs

e. Check that the logic flows correctly from the inputs

I03 Input number of paragraphs

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. * Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

I04 Input difficulty level

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. * Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

I05 Input for replacement words

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. * Check input validation

d. * Check for availability of the quit option

e. Check that the logic flows correctly from the inputs

    Correct Answer

        General
            Bug: word_loop() while condition not cancelled
            Fix: inserted else and reset flag

        End of Paragraph

        End of Game

    Incorrect Answer

        * Another Chance
            Bug: word_loop() fairy-count not found
            Fix: pass and return the fairy_count variable from the calling function
            Bug: word_loop() math.random() does not exist
            Fix: use random.random()
            Bug: sentence_loop() invalid use of . notation for dict reference
            Fix: used bracketed notation ["xx"]

I06 Input repeat same game

a. Ensure input prompt is clearly understandable

b. Check response to garbage input

c. Check input validation

d. Check for availability of the quit option

e. Check that the logic flows correctly from the inputs

I07 Input start another game

a. Ensure input prompt is clearly understandable

b. Check response to garbage input

c. Check input validation

d. Check for availability of the quit option

e. Check that the logic flows correctly from the inputs

I08 Input start another game

a. Ensure input prompt is clearly understandable

b. Check response to garbage input

c. Check input validation

d. Check for availability of the quit option

e. Check that the logic flows correctly from the inputs

### Random Branch Point Tests
### Playability Tests