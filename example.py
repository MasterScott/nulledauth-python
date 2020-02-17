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
