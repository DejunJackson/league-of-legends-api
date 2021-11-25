"""This module holds the utility function"""


def get_champ_dict():
    from champions.champion_scraper import champ_soup
    from champions.champion_class import Champion

    champs_soup = champ_soup.select("tbody > tr > td")

    # Deletes the last for rows from scraper (not needed)
    del champs_soup[-4:]
    stats = []
    champs = {}
    count = 0

    # iterates through scraped content and formats it
    for x in range(0, len(champs_soup)):
        removed_spaces = champs_soup[x].text.replace(
            ' ', '').replace('+', '').replace('%', '')

        # checks to see if string can be convert to float before adding to list
        try:
            stats.append(float(removed_spaces))
        except:
            stats.append(removed_spaces)

        # each champ needs 19 stats so it initiates a new Champion
        # object after iterating 19 times and passes in the stats
        # since they are scrapped in order
        if x == 0:
            continue
        elif x % 19 == 0:
            champ = Champion(*stats[count:x:1])
            champs[champ.name] = champ
            count = x

    return champs
