URL Shortener
=============
[![Python](https://img.shields.io/static/v1?logo=data:image/png;base64,R0lGODlhEAAQAPZkAOu7GOu+IfPBGvrHGf3LG//MHOvCKv/PI//PJP/QJf/QJv/TLf3SL//TLv/TL+vFNOjHPf/TMP/UMP3VNv/WN/rTOf/XOP/XOf/XOvnVPv/YOuzORf3ZQf/aQf/aQv/bQv/bQ//bRP3dSv/eS//fTf3eTv/fTv/iVf/jV//jWP/mYf/nYf/nYvLhbvXjb/3pav/rbDJghzZmkDZnkTVokjZpkzZplDdoljdqljlsljhslzltmTpvmzpwnDtwnDtwnTxxnj1zoD1zoj10oT50oj51oz92pUB4pkB4p0F5qEJ7qkN8q0N9rUN9rkR9rUR+rUV/r0aAsEaAsUaBskeBskiDtEiEtUiFtkmFt0qHuUqGukuIu0yJvEyKvE2LvkyKv06NwE+NwVCPw1KRxv///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAGUALAAAAAAQABAAAAemgGWCZWFaUkxGQDeDjIJdZFJKRD04jYxXkUQ+ODWWZV9XTEQ5Mjk4lYxjYVxVUEdAPDWnZScjGWViX1RQSrA1vzFlIx0Tn1dUkkCnNMEbxAtlx0tHnY0dFwsHZVLTNGUtLywnJiHYCARlTEpDZS4wLCnk5gUCgkM+Ze/xHRoLCAUFLMEzAeGBgQAAAHiKVy5CgoCeysiTkIAMuohlKjgsMACjx0GBAAA7&label=Python&message=3.9.0&color=brightgreen&link=https://www.python.org/)](https://www.python.org/) [![Flask](https://img.shields.io/static/v1?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAABLCAYAAAA4TnrqAAAKdElEQVR4nO2ceVRU9xXHBUSQRRAxLiggKpuICCqyCK4sKiCIKCKbgKBZFCOxGmNcQkgMmkVCkqohJkZM1Jg4bWybmK2mS2qXc9rEJKZpkya2SbRtrDkn6TnN7fte3s8zDLw38GaG98bDH98z23u/9/t95v7u7977mzcDiGhAv3om3TvgTNK9A84k3TvgTNK9A84k3TvgTFL8wPSfmx2pIEmFkholnZR0XtJnkq5JIlnX5PfOy8c0yucEObJvRoDlIilZUrOkC2ZAtOqC3Fay3PYNActb0npJH9gBkJI+lLRBvpZTwvKRdLekKw6EZKkr8jV9nAUWpsQqSZf6EJKlLsl90DQ9+woWHO9ZHSFZ6qxJw2LQF7ByJV02ACBLXZb7ZhhYDZK+NwAYJX0v91FXWPAJLQaA0VPtN/XAjzkKVqsBAPRWrXrAajLAwLWqqS9hVRtgwLaqvC9gxUv6zgCDtVXfSJriSFiDTQppy3OXaqjhyQwqaphGdz2/iI5/sUZvGD3Re5I8HAVrj9KFX/zXWrr94AIKmuBPi9ZMpiN/Wc3ATn+9Tm8g1rTTEbAiJf1X6aKn/rmWHvnFcgpPGEGBY3xo1tKJtLAmhh44u5Re+rehgX0rKcLesNrVLvr470soNX8CDRzkRu4ebjQ2YigFRwXQ9KxQumX/HNr/yxV08qs6vcEoqd2esKIl/U/tgnvfKKSgif5SawNofNxwqm5KZR82PTOEvIcMolFhfrRy6wx6+FwRHf20Sm84lsLYouwFq03pQrCWHScXU9qyieQ71JM8vAZSSHQAJeeNp7X70qnxx0to7soIhgjFpgVRQ1sGtb1fTocvVvL0NQAsksdoMyxfU+dSbyfteaWARo/3vw4D09DH34MCg3wofn4wbXh8Hu16MZdKtydSdlUMWxzO2Xw4k5Jzw6hwYzz7OgNAuyaP1SZYVUoXwCDnlUSyNQHUTcG+7Lfg2Nc8MIsh7XtjGbX/rZpeuFxHB/9USs2vF9KOF3KotjmNEjJC2LflrI2lJ/5QojcsksdqE6yXlRrHVJs8K4jKdsykrNWT2EowvR777UpeBR/6eRHd/Mhsjr1gWbAyQMLxAHn4wwpqfq2Q7j6xmJ58r4xOX9Ud1hlbYCFg+0ap8cgZIykpJ4x+8EwWNf0kn4HAokq2JbKTh6VNmT2GcupiGdq+N5dR6/mVtPt0Lj389vIu7RkAFsbqoRVWulrjmD6jxvnxKggogBMw0osmTB1OMSmjO1Y/Ccqzf63ioBXnwKIW106mLc9m89TUGU53StcKa5Naw/A9CAngr1zdXMj/Ji8aEz6Ups4bS9ulqYVjjn1WTSe+qOXnp67U0bbnFlLeLVN4RVSKuxD9t7yzopNOSNnAblMOLagI50ctIHAuZOW4TVphHVJr+Jk/V1LKkvEMy8t3EEfuoZOG0dIN8fToO8V030/z2U899UFFxzSTUh+kQK2/KaY727Pp+D+6zx8xILG6CgHYqh3T+bkWWPgCcG5ibrC1Yw9qhXVOreGTX9ZS8Zbp5OntTkOGedLYyAD2V09/VMlOe2F1TIcFfVnb6TxE+7e1zqVjn9d02+7wUE8eWP2BOddlDhHgxLGwOLwGjO6sU7xufr2Az82vj7UG65xWWJ+qNYycb8uRLPZZbgNdyS9wMIcSdXvTeKrBqsQUhGBVeA0nf2vLHDr6SddIXlhAZHJgl8+ElQlIwtKExDmW7+M9ABdfgPgcVnaia3XkE62wvrZm3rCSwvp4ikocSd5+HjRzcRhV3ZvCIcKhd8uo5dfFtPGH8/k5onlE9TtPdcRZbRfKu7QnLMBcGODBd0s7TSNhZbCU2r0p/BwQxHHQ1vbM61NWHC8eFUBBV7XCsuoLMJVgSbAoRO3Q8jumMbCiTQmUVjiRV0ZYIIJYTMt7X17Cj/BdlhUJYQGwEuGQAQCDtgSCYzBgAQtw0AZAWE45MbWFFECxHAYLyz9SF8RbWBk9vdwpbu5Yyr8tjmMtrIyNP8rj4iDiKMAB4D2vLqV7THn0/N87dxoDxGBgYebvmwOBzK0M0Mx9GUAIODgPrwUk8b5l+2b6zmHTUPiZVXclUsS0ETTI042nIywtsyKaCtZP5aje8hyslhsPzOdk2vx9MXBLh23u3IWVCWDmK6bwSebWhffFFBTnqoQQXznEwQshJEBynLhoHLm4DGAh70Nkv+3YQrY8WBEcO8IFHH/gj6W0ujGFo3pLJ45v3/IawiKE5QAG3oOVCZDCuYtjxRQ2d+7mVofPuhnPx1phvd0TWMJ3VexO4ghefNOYligxw8JQmQiNGUbV96VyPQsrIXJGyNKKdJbm0EE1KO1kXVc7qhAAM3SEF7m4ujAwlJcRzaMcg9dIi8TUg6NHLIbPDVR6PqQVVkNvLgRnj5wvtWACR/OAM3t5OFvd+sfmcuAaFhtI9U90hBI4B9MRFVXkkAYBpjndSe/txWA1qDwkLAjmOtdAd1fKqpzE0w8hBNIi1LAQXogqA5w9/BfSIwPAStcKS7VEoyQU8rA6IlAFLFjYjOxQhhaTOpqiZo7iso2wLghxFwAipNARlE0lGuiMlgvDWpDSoHKK3BFhRfnOJIaEOAzg5q+K4twSvg5TEMl1elE47wahQqEDLJuKf6plZTVhiqGMjPwQPmxk6BCeftCw0d5cOPQbPpj9GKL8+39WwCWbdQ+lM8wlt8bpsedoc1lZdcNCTdiEwNYXfBjq8ggdEINhUwMLAEIL7ARhWqJEjTwSMRhySJR5oM1PZ3JapFShQGIuYjgbwdplw0J1K8wqMGk6IYLHdpmofYldIKRGKBhiNwgVi8p7kjktEufBMrFSAvSy2xN4mmKzFhsgOAY+L6M8mktDSM5ttKo2k532DSeZrGyyWhMsYOvRbK5KwJrgwzAdzZNbWBt8FtKg7ccXcc3rjqcyOFHHJkfJnTMod90UTqHKdyVxTIdpjTaxQGAfABlB05l8zkcffKuIMws8WukfxhZtL1jQMVt9AqYlqqu7X8qlmvtTObpHsApwqN/DwrD1P9jHnZ+LrTX4NOSaqOljBwk1foQlKGFjc3dOcQSNmxzI/i9glDc/YsMXX4ZvgCf7Ryt9s+v2vdUfhvRG8EtHPl7NKybq+FgEUOdC6oOIH5sgqOljFQUwDBpTFpnBiJAh/L6o+wOs2LfEMShEYlpGJ3WEJ1gw8BMolf58K4+t735ypAna1Y7tf+SJ8Gv7f7WCfRsGiPI0hB1s+DIUGFF9RUYAENC0zBBaUBrFCwEsFekT/BjawpeBjAJO38oWm0N+cqT6YzYn1fuSPB0F60b7mWRcd2O0JyyoxgCDtVXlSuOzNyyo/6fdvYCFOxWc9aYB1bssHAELcjU51+0oLXKfVcflKFhCm03Gv9Fpc0/H42hYUJ6p/xa6XmmMpNcMAEjIsDdnmjv+MpP+t/2WmQx+26+5cFP3LlPf31C+y+REN5R3Bw1/I/CRAyGh7XpbIRkBlvn0TJH0oKSLdgB0UW4r1XQD/QmGkiz/XuV3pu7/XuVz+TNj/71Kv/ph9cPqh2VA6d4BZ5LuHXAm6d4BZ5LuHXAm6d4BZ9L/Afs4gGhdzuUTAAAAAElFTkSuQmCC&label=Flask&message=1.1.2&color=brightgreen&link=https://www.python.org/)](https://flask.palletsprojects.com/en/1.1.x/) [![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&link=https://mit-license.org/)](./LICENSE)

# Info

Developer: [Bradley Myers](https://github.com/BLM16)

Date created: 2021-01-27 | Last updated: 2021-01-27

## Setup

**Make sure you have Python (3.9.x) installed, and added to PATH.**

Create a virtual environment with the following command. All commands are to be run from the root directory of the project unless otherwise specified:

```bat
python -m venv venv
```

Install all the dependencies with the following commands:

```bat
.\venv\Scripts\activate.bat
pip install -r requirements.txt
deactivate
```

## License

This code is licensed under the [MIT License](./LICENSE)
