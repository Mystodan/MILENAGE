# Gruppeoppgave 1 - Milenage Implementasjon
Av: Christoffer Simonsen, Daniel Hao Huynh, Mikael Fossli <br>
[Milenage Implementation](https://github.com/Exzircon/MILENAGE/blob/Ref-deliver/oblig1.py) <br>
[Proof of work](https://github.com/Exzircon/MILENAGE/blob/Ref-deliver/Proof%20of%20work.pdf) <br>
[Merkle trær](https://github.com/Exzircon/MILENAGE/blob/Ref-deliver/merkle%20tr%C3%A6r.pdf)

Dette er vår implementasjon av Milenage, 3GPP autentisering- og nøkkelgenererings- funksjoner. Milenage er basert på AES (Rjindael) og vi har følgt 3GPP- TS 35.205 - 35.208 og TR 35.909

### Test resultater
Alle tester bestått etter spesifikasjoner
  - f0 – pseudo-random funksjon (128-bit nummer)
  - f1 – nettverk autentiseringsfunksjon
  - f2 – responsfunksjon
  - f3 – kdf for CK
  - f4 – kdf for IK
  - f5 – kdf for AK 
> alle funksjonene bestod testdata fra spesifikasjonen 3GPP TS 35.208

for å reprodusere resultatene, tast inn fra rot: <br>
```sh
python -m unittest
```
