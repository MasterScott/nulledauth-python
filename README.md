# Nulledauth.net python class
## Why?
I have done this class in order to keep my mental health good, 
nulledauth.net docs are confusing for me, so after asking several 
times to Jackdev I was able to make this work on python. 
Before that I got the class made in C# from animu and CoffeeDev(Germany)

## How is the HWID obtained?

The hwid is obtained using:
> wmic cpu get processorid

this can be run on a command line to get the id of the CPU.
## How do I use it?

It's easy just clone / download the content of **auth.py**
and import it, if you don't know what's **venv** folder, it's just a virtual
environment, so you can run the class in any machine without having to be worry about the modules.

#### Make sure to install requests if you don't use the virtual environment
> pip install requests

this will work in most of cases, if you need help to install requests message me.

# Example of usage
```python
import auth

print("Enter your nulled auth")
print(">>> ", end="")
nulled_auth = input("")

program_id = "1196002"
secret_id = "INJYURQMABDCFODZ0LFBVR98QRZKZZIP"
check_auth = auth.Auth(nulled_auth, program_id, secret_id)

value = check_auth.check()

if value:
    print("Auth guaranteed")
elif value is False:
    print("You are not authorized")
    exit()
else:
    print("Could not connect to the server")
    exit()

```

### Take in mind that this is an example and the program_id and secret_id was created for this example, to get your own program_id and secret_id go to  [NulledAuth](nulledauth.net).

