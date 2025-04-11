import pandas as pd
import pytest

def test_rating_percentage_calculation():
    # Sample DataFrame
    data = {
        'positive_ratings': [80, 50],
        'negative_ratings': [20, 50]
    }
    df = pd.DataFrame(data)

    # Expected result
    expected_percentages = [80.0, 50.0]

    # Perform calculation
    df['total_ratings'] = df['positive_ratings'] + df['negative_ratings']
    df['rating_percentage'] = (df['positive_ratings'] / df['total_ratings']) * 100

    # Test
    assert df['rating_percentage'].tolist() == expected_percentages
