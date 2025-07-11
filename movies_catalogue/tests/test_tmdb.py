from unittest.mock import Mock
import tmdb_client

def test_get_single_movie(monkeypatch):
    expected_result = {"id": 123, "title": "Test Movie"}
    mock_call = Mock(return_value=expected_result)
    monkeypatch.setattr(tmdb_client, "call_tmdb_api", mock_call)

    result = tmdb_client.get_single_movie(123)
    assert result == expected_result
    mock_call.assert_called_once_with("movie/123?language=pl-PL")

def test_get_movie_cast(monkeypatch):
    expected_cast = [{"name": "Actor 1"}, {"name": "Actor 2"}]
    mock_call = Mock(return_value={"cast": expected_cast})
    monkeypatch.setattr(tmdb_client, "call_tmdb_api", mock_call)

    result = tmdb_client.get_movie_cast(123)
    assert result == expected_cast
    mock_call.assert_called_once_with("movie/123/credits")

def test_get_movies_list(monkeypatch):
    expected_data = {"results": [{"id": 1}, {"id": 2}]}
    mock_call = Mock(return_value=expected_data)
    monkeypatch.setattr(tmdb_client, "call_tmdb_api", mock_call)

    result = tmdb_client.get_movies_list("popular")
    assert result == expected_data
    mock_call.assert_called_once_with("movie/popular")

def test_get_movies(monkeypatch):
    mock_movies = {"results": [{"id": 1}, {"id": 2}, {"id": 3}]}
    mock_call = Mock(return_value=mock_movies)
    monkeypatch.setattr(tmdb_client, "get_movies_list", mock_call)

    result = tmdb_client.get_movies(2)
    assert result == [{"id": 1}, {"id": 2}]
    mock_call.assert_called_once_with("popular")