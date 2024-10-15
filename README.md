# Group Assignment 1 - Milenage Implementasjon
Av: Christoffer Simonsen, Daniel Hao Huynh, Mikael Fossli <br>
[Proof of work](https://github.com/Exzircon/MILENAGE/blob/Ref-deliver/Proof%20of%20work.pdf) <br>
[Merkle trær](https://github.com/Exzircon/MILENAGE/blob/Ref-deliver/merkle%20tr%C3%A6r.pdf)

### Test results
Alle tester bestått etter spesifikasjoner
  - f0 – the pseudo-random function (128-bit number)
  - f1 – the network authentication function
  - f2 – response function
  - f3 – kdf for CK
  - f4 – kdf for IK
  - f5 – kdf for AK 
> all passed the specified tests from TS 35.208

for å reprodusere resultatene, tast inn fra rot: <br>
```sh
python -m unittest
```
