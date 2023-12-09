from film_atr_manager import FilmManager
from domain.validator import FilmValidator
from domain.validator import ClientValidator
from clienti_atr_manager import ClientiManager
from consola import Console
from clienti_atr_manager import test_add_client

film_validator= FilmValidator()
film_atr_manager = FilmManager(film_validator)
client_validaotr= ClientValidator()
clienti_atr_manager = ClientiManager(client_validaotr)
console= Console(film_atr_manager, clienti_atr_manager)
test_add_client()

console.run()