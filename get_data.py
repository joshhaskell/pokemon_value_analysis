import pandas as pd
from pokemontcgsdk import Card, RestClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure the RestClient with the API key
pokemon_tcg_api_key = os.getenv('pokemon_tcg_api_key')
RestClient.configure(pokemon_tcg_api_key)

def extract_basic_card_data(card):
    """
    Extracts basic information from a Pokémon card.

    Parameters:
        card (Card): A Card object from the Pokémon TCG SDK.

    Returns:
        dict: A dictionary containing basic information about the card.
    """
    data = {
        'card_id': card.id,
        'name': card.name,
        'hp': card.hp,
        'rarity': card.rarity,
        'artist': card.artist,
        'supertype': card.supertype,
        'evolvesFrom': card.evolvesFrom,
        'flavorText': card.flavorText,
        'convertedRetreatCost': card.convertedRetreatCost,
        'regulationMark': card.regulationMark,
        'rules': ', '.join(card.rules) if card.rules else None,
        'image_small': card.images.small if card.images else None,
        'image_large': card.images.large if card.images else None,
        'set_id': card.set.id if card.set else None,
        'set_name': card.set.name if card.set else None,
        'set_series': card.set.series if card.set else None,
        'set_printedTotal': card.set.printedTotal if card.set else None,
        'set_total': card.set.total if card.set else None,
        'set_releaseDate': card.set.releaseDate if card.set else None,
        'set_updatedAt': card.set.updatedAt if card.set else None,
        'set_legalities_unlimited': card.set.legalities.unlimited if card.set and card.set.legalities else None,
        'set_legalities_expanded': card.set.legalities.expanded if card.set and card.set.legalities else None,
        'set_legalities_standard': card.set.legalities.standard if card.set and card.set.legalities else None,
        'set_image_symbol': card.set.images.symbol if card.set and card.set.images else None,
        'set_image_logo': card.set.images.logo if card.set and card.set.images else None,
        'number': card.number,
        'ancientTrait_name': card.ancientTrait.name if card.ancientTrait else None,
        'ancientTrait_text': card.ancientTrait.text if card.ancientTrait else None,
        'type_1': card.types[0] if card.types and len(card.types) > 0 else None,
        'type_2': card.types[1] if card.types and len(card.types) > 1 else None,
        'subtype_1': card.subtypes[0] if card.subtypes and len(card.subtypes) > 0 else None,
        'subtype_2': card.subtypes[1] if card.subtypes and len(card.subtypes) > 1 else None,
        'subtype_3': card.subtypes[2] if card.subtypes and len(card.subtypes) > 2 else None,
        'subtype_4': card.subtypes[3] if card.subtypes and len(card.subtypes) > 3 else None,
        'nationalPokedexNumber': card.nationalPokedexNumbers[0] if card.nationalPokedexNumbers and len(card.nationalPokedexNumbers) == 1 else None,
    }
    return data

def extract_abilities_data(card):
    """
    Extracts abilities information from a Pokémon card.

    Parameters:
        card (Card): A Card object from the Pokémon TCG SDK.

    Returns:
        list: A list of dictionaries containing abilities information.
    """
    abilities = []
    if card.abilities:
        for ability in card.abilities:
            abilities.append({
                'card_id': card.id,
                'ability_name': ability.name,
                'ability_text': ability.text,
                'ability_type': ability.type,
            })
    return abilities

def extract_attacks_data(card):
    """
    Extracts attacks information from a Pokémon card.

    Parameters:
        card (Card): A Card object from the Pokémon TCG SDK.

    Returns:
        list: A list of dictionaries containing attacks information.
    """
    attacks = []
    if card.attacks:
        for attack in card.attacks:
            attacks.append({
                'card_id': card.id,
                'attack_name': attack.name,
                'attack_cost': ', '.join(attack.cost),
                'attack_convertedEnergyCost': attack.convertedEnergyCost,
                'attack_damage': attack.damage,
                'attack_text': attack.text,
            })
    return attacks

def extract_prices_data(card):
    """
    Extracts prices information from a Pokémon card.

    Parameters:
        card (Card): A Card object from the Pokémon TCG SDK.

    Returns:
        list: A list of dictionaries containing prices information.
    """
    prices = []
    if card.tcgplayer and card.tcgplayer.prices:
        price_data = card.tcgplayer.prices
        if price_data.normal:
            prices.append({
                'card_id': card.id,
                'price_type': 'normal',
                'low': price_data.normal.low,
                'mid': price_data.normal.mid,
                'high': price_data.normal.high,
                'market': price_data.normal.market,
                'directLow': price_data.normal.directLow,
            })
        if price_data.holofoil:
            prices.append({
                'card_id': card.id,
                'price_type': 'holofoil',
                'low': price_data.holofoil.low,
                'mid': price_data.holofoil.mid,
                'high': price_data.holofoil.high,
                'market': price_data.holofoil.market,
                'directLow': price_data.holofoil.directLow,
            })
        if price_data.reverseHolofoil:
            prices.append({
                'card_id': card.id,
                'price_type': 'reverseHolofoil',
                'low': price_data.reverseHolofoil.low,
                'mid': price_data.reverseHolofoil.mid,
                'high': price_data.reverseHolofoil.high,
                'market': price_data.reverseHolofoil.market,
                'directLow': price_data.reverseHolofoil.directLow,
            })
        if price_data.firstEditionHolofoil:
            prices.append({
                'card_id': card.id,
                'price_type': 'firstEditionHolofoil',
                'low': price_data.firstEditionHolofoil.low,
                'mid': price_data.firstEditionHolofoil.mid,
                'high': price_data.firstEditionHolofoil.high,
                'market': price_data.firstEditionHolofoil.market,
                'directLow': price_data.firstEditionHolofoil.directLow,
            })
        if price_data.firstEditionNormal:
            prices.append({
                'card_id': card.id,
                'price_type': 'firstEditionNormal',
                'low': price_data.firstEditionNormal.low,
                'mid': price_data.firstEditionNormal.mid,
                'high': price_data.firstEditionNormal.high,
                'market': price_data.firstEditionNormal.market,
                'directLow': price_data.firstEditionNormal.directLow,
            })
    return prices

def extract_resistances_data(card):
    """
    Extracts resistances information from a Pokémon card.

    Parameters:
        card (Card): A Card object from the Pokémon TCG SDK.

    Returns:
        list: A list of dictionaries containing resistances information.
    """
    resistances = []
    if card.resistances:
        for resistance in card.resistances:
            resistances.append({
                'card_id': card.id,
                'resistance_type': resistance.type,
                'resistance_value': resistance.value,
            })
    return resistances

def extract_weaknesses_data(card):
    """
    Extracts weaknesses information from a Pokémon card.

    Parameters:
        card (Card): A Card object from the Pokémon TCG SDK.

    Returns:
        list: A list of dictionaries containing weaknesses information.
    """
    weaknesses = []
    if card.weaknesses:
        for weakness in card.weaknesses:
            weaknesses.append({
                'card_id': card.id,
                'weakness_type': weakness.type,
                'weakness_value': weakness.value,
            })
    return weaknesses

def main():
    # Fetch all cards
    all_cards = Card.all()

    # Extract data into separate lists
    basic_data = [extract_basic_card_data(card) for card in all_cards]
    abilities_data = [ability for card in all_cards for ability in extract_abilities_data(card)]
    attacks_data = [attack for card in all_cards for attack in extract_attacks_data(card)]
    prices_data = [price for card in all_cards for price in extract_prices_data(card)]
    resistances_data = [resistance for card in all_cards for resistance in extract_resistances_data(card)]
    weaknesses_data = [weakness for card in all_cards for weakness in extract_weaknesses_data(card)]

    # Create DataFrames
    basic_df = pd.DataFrame(basic_data)
    abilities_df = pd.DataFrame(abilities_data)
    attacks_df = pd.DataFrame(attacks_data)
    prices_df = pd.DataFrame(prices_data)
    resistances_df = pd.DataFrame(resistances_data)
    weaknesses_df = pd.DataFrame(weaknesses_data)

    # Count unique occurrences
    abilities_count = abilities_df.groupby('card_id').size().reset_index(name='num_abilities')
    attacks_count = attacks_df.groupby('card_id').size().reset_index(name='num_attacks')
    resistances_count = resistances_df.groupby('card_id').size().reset_index(name='num_resistances')
    weaknesses_count = weaknesses_df.groupby('card_id').size().reset_index(name='num_weaknesses')

    # Combine DataFrames
    dfs = [abilities_count, attacks_count, resistances_count, weaknesses_count, prices_df]

    final_df = basic_df.copy()
    for df in dfs:
        final_df = final_df.merge(df, on='card_id', how='left')

    # Create a unique identifier combining card_id and price_type
    final_df['price_type'] = final_df['price_type'].fillna('unknown')
    final_df['card_type_id'] = final_df['card_id'] + '_' + final_df['price_type']
    final_df = final_df.drop(columns=['card_id']) # Drop the original card_id column and will use the new card_type_id as the unique identifier

    # Reorder the columns
    cols = ['card_type_id'] + [col for col in final_df.columns if col not in ['card_type_id']]
    final_df = final_df[cols]

    # Save as csv
    final_df.to_csv('data/raw_pokemon_data.csv', index=False)
    print("The raw dataframe has been saved to 'data/final_pokemon_data.csv'.")

if __name__ == "__main__":
    main()