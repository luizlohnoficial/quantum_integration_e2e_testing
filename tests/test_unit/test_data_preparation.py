from data_preparation import load_data


def test_load_data():
    config = {
        'assets': [{'name': 'A'}],
        'covariance_matrix': [[1]]
    }
    assets, covariance = load_data(config)
    assert assets[0]['name'] == 'A'
    assert len(covariance) == 1 and len(covariance[0]) == 1
