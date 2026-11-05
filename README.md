# payment-discount-split

## Français

Séparer escompte et règlement sans perdre les centimes.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m payment_discount_split examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Calcule un escompte contractuel déclaré en points de base, arrondit une fois au total puis répartit par plus forts restes ; conserve exactement les centimes.

### Limites

Montants positifs dans une devise, sans recalcul fiscal ni décision d’éligibilité à l’escompte ; règle d’arrondi explicitement choisie, pas norme universelle.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Separate settlement discounts and payments without losing cents.

Synthetic data; no network access or secret required.

```sh
python -m payment_discount_split examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Computes a declared contractual discount in basis points, rounds once at total level then allocates by largest remainders; exactly conserves cents.

### Limits

Positive amounts in one currency, no tax recalculation or discount eligibility decision; explicitly chosen rounding rule, not a universal standard.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Separar descuentos y pagos sin perder céntimos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m payment_discount_split examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Calcula descuento contractual declarado en puntos básicos, redondea una vez el total y reparte por restos mayores; conserva céntimos exactamente.

### Límites

Importes positivos en una moneda, sin recálculo fiscal ni decisión de elegibilidad; regla de redondeo explícita, no estándar universal.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.python.org/3/library/fractions.html
