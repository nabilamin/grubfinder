# Grubfinder
## Development team
This project was created for UMGC CMSC 495 7386 by:
- Alemayehu Berihun
- Evan Bridges
- Jonathan George
- Nabil Amin
- Tristan Zimmerman

## Who is Grubfinder for?
People who organize food orders are burdened with having to accommodate a spectrum of tastebuds and palettes. 
The sheer number of ordering possibilities often results in indecisiveness and prolonged deliberation. 
Food should be a pleasurable experience, but it easily becomes an overwhelming challenge.

Use Grubfinder to reduce the indecision of choosing a place to eat.

## What does Grubfinder do?

GrubFinder aims to reduce the cognitive load and decision fatigue associated with organizing group food orders. The primary objectives of the project are to:

1. Find highly rated, local restaurants that are currently open. 
2. Facilitate private group voting for the best restaurant to order. 
3. Guide the decision on a place to eat. 

This app allows a group of friends, coworkers, or family members to privately vote on a restaurant of choice. 
GrubFinder uses the Yelp API to find highly rated, local restaurants that are open for dine-in or take-out. 
After votes have been cast, the restaurant with the most votes wins. 

When it’s time to order food, GrubFinder guides the group to a decision.

## How does Grubfinder work?
When the **host** needs to order food for a group, Grubfinder.io helps them identify a restaurant from which to order by polling the individuals in their group.
Grubfinder uses a combination of web scraping and the Yelp API to identify quality restaurants in the area.
The voting session is configured by the host, allowing them to set the type of food to include and how expensive the restaurants are.
The host can also select, from a list of restaurants, which ones to include in the vote.
Upon the start of a new session, the host is provided with a code that should be shared with participants who wish to submit their votes.

The **participants** navigate to Grubfinder and enter the code join the host's session. Once a participant joins, they vote “yes” or “no” on each restaurant option that the host included in the session.

The host ends the session and views the restaurant with the most votes. When there the votes are equally distributed across multiple restaurants, the application will break the tie by choosing a winner at random.
