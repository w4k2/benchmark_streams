# Benchmark data streams

## TLDR;

W katalogu `datasets` znajdują się wygenerowane strumienie danych, w katalogu `files` poglądowe krzywe uczenia dla klasyfikatora MLP (100 sztucznych neuronów w warstwie ukrytej). Każdy strumień jest problemem binarnym o siedmiu atrybutach, o długości 100000 wzorców. Dzielą się na trzy grupy:

- rozpoczynające się od `s_` : strumienie bazowe bez dryfów, po trzy z każdego z trzech generatorów bazowych (`hyp`, `led` i `rbf`), o trzech poziomach trudności problemu (`r1`, `r2` i `r3`),
- rozpoczynające się od `sd_` : dryfy nagłe, zawierające po cztery dryfy pomiędzy generatorami bazowymi oznaczonymi w nazwie pliku,
- rozpoczynające się od `id_` : dryfy inkrementalne (płynne), zawierające po cztery dryfy pomiędzy generatorami bazowymi oznaczonymi w nazwie pliku.
