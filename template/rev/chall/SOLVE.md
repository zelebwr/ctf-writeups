<!--
This banner uses Shields.io. Edit the text and color to match your challenge.
- Replace [CATEGORY] with the challenge category (e.g., Cryptography).
- Replace [CHALLENGE_NAME] with the name of the challenge.
- Replace [POINTS] with the point value.
- Change the color hex code `5A91E4` to your preference.
-->

![Challenge Banner](https://img.shields.io/badge/[CATEGORY]-[CHALLENGE_NAME]-[POINTS]?style=for-the-badge&logo=github-sponsors&logoColor=white&color=5A91E4)

_Write-up by zelebwr (BNB) &mdash; July 26, 2025_

---

## 📝 Metadata & Synopsis

| Field              | Value                                                                |
| ------------------ | -------------------------------------------------------------------- |
| **Event**          | `ShaktiCTF 2025` / `PicoCTF`                                         |
| **Category**       | `Cryptography`                                                       |
| **Points**         | `[POINTS]`                                                           |
| **Challenge Link** | [Link to Challenge](https://play.picoctf.org/practice/challenge/...) |
| **Status**         | ✅ Solved                                                            |

### Challenge Description

> [PASTE THE OFFICIAL CHALLENGE DESCRIPTION HERE]

### Provided Artifacts

-   `file`
-   `Instance`
-   `Deployment Script`
-   _(Delete what's not relevant)_

---

## 📚 Table of Contents

-   [Reconnaissance & Initial Analysis](#reconnaissance--initial-analysis)
-   [Vulnerability Exploitation](#vulnerability-exploitation)
-   [Final Payload / Script](#-final-payload--script)
-   [Flag](#-flag)
-   [Lessons Learned](#-lessons-learned)
-   [Mitigation](#️-mitigation)
-   [Sources](#-sources)

---

## 🔎 Reconnaissance & Initial Analysis {#reconnaissance--initial-analysis}

_Initial steps taken to understand the challenge. What kind of file is it? What service is running? What are the first thoughts?_

For example:

-   Ran `file` and `strings` on the provided binary.
-   Connected to the `netcat` instance to observe the initial interaction.
-   Opened the web page and inspected the source code and network traffic.

```bash
# Example commands
file challenge_binary
strings challenge_binary | head
```

---

## 🔓 Vulnerability Exploitation {#vulnerability-exploitation}

_The step-by-step process of finding and exploiting the vulnerability. Break this down into logical stages._

### Stage 1: [Name of the First Step]

_Detailed explanation of the first part of the exploit process. You can reference a source like this.[^1]_

!!! tip "Key Insight"
_This is where the "aha!" moment happened. What was the key piece of information or technique that cracked this stage?_

### Stage 2: [Name of the Second Step]

_Continuing the exploitation process... You can reference another source like this.[^2]_

!!! warning "Potential Rabbit Hole"
_Did you try something that didn't work? Documenting dead ends is just as important as the solution path. It shows a thorough process._

---

## 👨‍💻 Final Payload / Script {#final-payload--script}

_The final script or one-liner used to retrieve the flag._

```python
# solve.py
from pwn import *

# Your final script here
p = remote('example.com', 1337)
p.sendline(b'payload')

flag = p.recvall()
log.info(f"Flag: {flag.decode()}")
```

---

## 🏁 Flag {#flag}

The flag obtained after successful exploitation.

```
ctf{[FLAG_HERE]}
```

---

## 🧠 Lessons Learned {#lessons-learned}

_This is one of the most important sections. What did you learn from this challenge?_

-   Learned about a specific cryptographic vulnerability like [Vulnerability Name].
-   Gained experience with a new tool like `[Tool Name]`.
-   Understood the importance of sanitizing user input to prevent [Attack Type].

---

## 🛡️ Mitigation {#mitigation}

_How could this vulnerability be fixed in a real-world application?_

-   **Input Validation**: The server should properly validate and sanitize all input received from the client.
-   **Using Secure Libraries**: The application should use up-to-date and secure libraries for handling cryptographic operations instead of rolling its own.
-   **Principle of Least Privilege**: The service should run with the minimum permissions necessary.

---

## 📖 Sources {#sources}

[^1]: [Link to a relevant blog post or Stack Overflow answer](https://example.com)
[^2]: [Documentation for a specific tool or library](https://docs.example.com)
