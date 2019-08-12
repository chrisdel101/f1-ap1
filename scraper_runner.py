from models import driver_model, team_model
from slugify import slugify, Slugify
from utilities import utils
from utilities.scraper import team_scraper, driver_scraper
_slugify = Slugify()
_slugify = Slugify(to_lower=True)
_slugify.separator = '_'


def main():
    scrape_teams()
    scrapte_drivers()


# - scrapes all drivers & inserts into DB
def scrape_drivers():
    # -get all driver names
    all_drivers = driver_scraper.scrape_all_driver_names()
    # print(alldrivers)
    standings = driver_scraper.scrape_all_drivers_standings()
    # - loop over names
    for driver in all_drivers:
        # slugify name
        driver_slug = slugify(driver).lower()
        # scrape each driver
        new_driver_dict = driver_scraper.apply_scraper_set1_complete_driver(
            driver_slug)
        # add etxra data to obj
        new_driver_dict = driver_scraper.apply_scraper_set2_complete_driver(
            driver_slug, new_driver_dict)
        # print(new_driver_dict)
        name_slug = slugify(new_driver_dict.get('driver_name').lower())
        i = 0
        # match standing with current driver
        while standings:
            # print('before', len(standings))
            # print(standings[i])
            # print('name', name_slug)
            # print(i)
            if name_slug == standings[i].get('name_slug'):
                new_driver_dict['points'] = standings[i].get('points')
                new_driver_dict['position'] = standings[i].get('position')
                # remove item from list so not looped over again
                standings.pop(i)
                # print('after', len(standings))
                # print('REMOVE', standings[i])
                i = 0
                print('\n')
                break
            i = i + 1
        # print(new_driver_dict)
        # - insert on scrape into DB
        d = driver_model.Driver.new(new_driver_dict)
        if d.exists(driver_slug):
            d.delete(driver_slug)
        d.insert()

        # scrape and add to DB


def scrape_teams():
    # -get all driver names - returns dict w/ name and slug
    all_teams = team_scraper.scrape_all_team_names()
    # - loop over names
    for team in all_teams:
        # convert to url_slug
        url_name_slug = utils.create_url_name_slug(team)
        # scrape each team
        new_dict = team_scraper.scrape_single_team_stats(url_name_slug)
        # add slug to model
        new_dict['name_slug'] = team['name_slug']
        # add url slug to model
        new_dict['url_name_slug'] = url_name_slug
        # add main_ing to current team obj
        new_dict = team_scraper.iterate_teams_markup(new_dict)

    # - insert on scrape into DB
        d = team_model.Team.new(new_dict)
        if d.exists(team['name_slug']):
            d.delete(team['name_slug'])
        d.insert()


def tester():
    print("\n")
    x = team_model.Team.query.filter_by(name_slug="williams").one()
    print(x.drivers[0])
    print("\n")
