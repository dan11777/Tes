
import requests

__ENDPOINT_URL__: str = "https://garden.squareweb.app/api"

class Pakundo:
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
        
    def login(self, email, password) -> int:
        payload = {
            "account_email": email,
            "account_password": password
        }
        params = {
            "key": self.access_key,
            "acc_email": email,
            "acc_pass": password
        } 
        response = requests.post(f"{__ENDPOINT_URL__}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")


    def change_email(self, new_email):
        decoded_email = urllib.parse.unquote(new_email)
        payload = {
            "account_auth": self.auth_token,
            "new_email": decoded_email
        }
        params = {
            "key": self.access_key,
            "new_email": decoded_email
        } 
        response = requests.post(f"{__ENDPOINT_URL__}/change_email", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("new_token"):
            self.auth_token = response_decoded["new_token"]
        return response_decoded.get("ok")
    
    def change_password(self, new_password):
        payload = { "account_auth": self.auth_token, "new_password": new_password }
        params = { "key": self.access_key, "new_password": new_password }
        response = requests.post(f"{__ENDPOINT_URL__}/change_password", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("new_token"):
            self.auth_token = response_decoded["new_token"]
        return response_decoded.get("ok")
        
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        requests.post(f"{__ENDPOINT_URL__}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        params = { "key": self.access_key }
        response = requests.get(f"{__ENDPOINT_URL__}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_coins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_coins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_localid(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_id", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_player_car(self, car_id) -> any:
        payload = { "account_auth": self.auth_token, "car_id": car_id }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/get_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/delete_friends", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_w16(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_w16", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_horns(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_horns", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def disable_engine_damage(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/disable_damage", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlimited_fuel", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_wins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_wins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_loses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_houses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_smoke(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_smoke", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_all_lamborghinis(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_lamborghinis", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_all_cars(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_all_cars_siren(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars_siren", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def account_clone(self, account_email, account_password) -> bool:
        payload = { "account_auth": self.auth_token, "account_email": account_email, "account_password": account_password }
        params = { "key": self.access_key, "account_email": account_email, "account_password": account_password }
        response = requests.post(f"{__ENDPOINT_URL__}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def set_player_plates(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_plates", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_wheels(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_wheels", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_male(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_hat_m(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_hat_m", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def rmhm(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/rmhm", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_topm(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_topm", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_topmz(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_topmz", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_topmx(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_topmx", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_female(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def rmhfm(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/rmhfm", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_topf(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_topf", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_topfz(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_topfz", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def hack_car_speed(self, car_id, new_hp, new_inner_hp, new_nm, new_torque):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/hack_car_speed", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_animations(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_animations", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def max_max1(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/max_max1", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def max_max2(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/max_max2", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def millage_car(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/millage_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def millage_car(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/millage_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def brake_car(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/brake_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def headlight(self, car_id):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/headlight", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_crown(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_crown", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_cls(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_cls", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def rear_bumper(self, car_id):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/rear_bumper", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def front_bumper(self, car_id):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/front_bumper", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def telmunnongodz(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/telmunnongodz", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def telmunnongonz(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/telmunnongonz", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def incline(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/incline", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def copy_livery(self, source_car_id, target_car_id):
        payload = {
        "account_auth": self.auth_token,
        "source_car_id": source_car_id,
        "target_car_id": target_car_id,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/copy_livery", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def clone_car_to(self, source_car_id, target_email, target_password):
        payload = {
        "account_auth": self.auth_token,
        "source_car_id": source_car_id,
        "target_email": target_email,
        "target_password": target_password
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/clone_car_to", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def copy_car_to(self, source_car_id, target_email, target_password, target_car_id):
        payload = {
        "account_auth": self.auth_token,
        "source_car_id": source_car_id,
        "target_email": target_email,
        "target_password": target_password,
        "target_car_id": target_password
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/copy_car_to", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def shittin(self) -> bool: 
        payload = { "account_auth": self.auth_token } 
        params = { "key": self.access_key } 
        response = requests.post(f"{__ENDPOINT_URL__}/shittin", params=params, data=payload) 
        response_decoded = response.json() 
        return response_decoded.get("ok")

# GOODMAFIA PROPERTY
import base64
encoded_data = '''IyBHT09ETUFGSUEgUFJPUEVSVFkKaW1wb3J0IGJhc2U2NAplbmNvZGVkX2RhdGEgPSAnJydhVzF3YjNKMElISmxjWFZsYzNSekNncGZYMFZPUkZCUFNVNVVYMVZTVEY5Zk9pQnpkSElnUFNBaWFIUjBjSE02THk5bllYSmtaVzR1YzNGMVlYSmxkMlZpTG1Gd2NDOWhjR2tpQ2dwamJHRnpjeUJRWVd0MWJtUnZPZ29nSUNBZ1pHVm1JRjlmYVc1cGRGOWZLSE5sYkdZc0lHRmpZMlZ6YzE5clpYa3BJQzArSUU1dmJtVTZDaUFnSUNBZ0lDQWdjMlZzWmk1aGRYUm9YM1J2YTJWdUlEMGdUbTl1WlFvZ0lDQWdJQ0FnSUhObGJHWXVZV05qWlhOelgydGxlU0E5SUdGalkyVnpjMTlyWlhrS0lDQWdJQ0FnSUNBS0lDQWdJR1JsWmlCc2IyZHBiaWh6Wld4bUxDQmxiV0ZwYkN3Z2NHRnpjM2R2Y21RcElDMCtJR2x1ZERvS0lDQWdJQ0FnSUNCd1lYbHNiMkZrSUQwZ2V3b2dJQ0FnSUNBZ0lDQWdJQ0FpWVdOamIzVnVkRjlsYldGcGJDSTZJR1Z0WVdsc0xBb2dJQ0FnSUNBZ0lDQWdJQ0FpWVdOamIzVnVkRjl3WVhOemQyOXlaQ0k2SUhCaGMzTjNiM0prQ2lBZ0lDQWdJQ0FnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzS0lDQWdJQ0FnSUNBZ0lDQWdJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVN3S0lDQWdJQ0FnSUNBZ0lDQWdJbUZqWTE5bGJXRnBiQ0k2SUdWdFlXbHNMQW9nSUNBZ0lDQWdJQ0FnSUNBaVlXTmpYM0JoYzNNaU9pQndZWE56ZDI5eVpBb2dJQ0FnSUNBZ0lIMGdDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMkZqWTI5MWJuUmZiRzluYVc0aUxDQndZWEpoYlhNOWNHRnlZVzF6TENCa1lYUmhQWEJoZVd4dllXUXBDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDQTlJSEpsYzNCdmJuTmxMbXB6YjI0b0tRb2dJQ0FnSUNBZ0lHbG1JSEpsYzNCdmJuTmxYMlJsWTI5a1pXUXVaMlYwS0NKdmF5SXBPZ29nSUNBZ0lDQWdJQ0FnSUNCelpXeG1MbUYxZEdoZmRHOXJaVzRnUFNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrTG1kbGRDZ2lZWFYwYUNJcENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSmxjbkp2Y2lJcENnb0tJQ0FnSUdSbFppQmphR0Z1WjJWZlpXMWhhV3dvYzJWc1ppd2dibVYzWDJWdFlXbHNLVG9LSUNBZ0lDQWdJQ0JrWldOdlpHVmtYMlZ0WVdsc0lEMGdkWEpzYkdsaUxuQmhjbk5sTG5WdWNYVnZkR1VvYm1WM1gyVnRZV2xzS1FvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0NpQWdJQ0FnSUNBZ0lDQWdJQ0poWTJOdmRXNTBYMkYxZEdnaU9pQnpaV3htTG1GMWRHaGZkRzlyWlc0c0NpQWdJQ0FnSUNBZ0lDQWdJQ0p1WlhkZlpXMWhhV3dpT2lCa1pXTnZaR1ZrWDJWdFlXbHNDaUFnSUNBZ0lDQWdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNLSUNBZ0lDQWdJQ0FnSUNBZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU3dLSUNBZ0lDQWdJQ0FnSUNBZ0ltNWxkMTlsYldGcGJDSTZJR1JsWTI5a1pXUmZaVzFoYVd3S0lDQWdJQ0FnSUNCOUlBb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOWphR0Z1WjJWZlpXMWhhV3dpTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUdsbUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p1WlhkZmRHOXJaVzRpS1RvS0lDQWdJQ0FnSUNBZ0lDQWdjMlZzWmk1aGRYUm9YM1J2YTJWdUlEMGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpGc2libVYzWDNSdmEyVnVJbDBLSUNBZ0lDQWdJQ0J5WlhSMWNtNGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDNW5aWFFvSW05cklpa0tJQ0FnSUFvZ0lDQWdaR1ZtSUdOb1lXNW5aVjl3WVhOemQyOXlaQ2h6Wld4bUxDQnVaWGRmY0dGemMzZHZjbVFwT2dvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0lDSmhZMk52ZFc1MFgyRjFkR2dpT2lCelpXeG1MbUYxZEdoZmRHOXJaVzRzSUNKdVpYZGZjR0Z6YzNkdmNtUWlPaUJ1WlhkZmNHRnpjM2R2Y21RZ2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVN3Z0ltNWxkMTl3WVhOemQyOXlaQ0k2SUc1bGQxOXdZWE56ZDI5eVpDQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMk5vWVc1blpWOXdZWE56ZDI5eVpDSXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdhV1lnY21WemNHOXVjMlZmWkdWamIyUmxaQzVuWlhRb0ltNWxkMTkwYjJ0bGJpSXBPZ29nSUNBZ0lDQWdJQ0FnSUNCelpXeG1MbUYxZEdoZmRHOXJaVzRnUFNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrV3lKdVpYZGZkRzlyWlc0aVhRb2dJQ0FnSUNBZ0lISmxkSFZ5YmlCeVpYTndiMjV6WlY5a1pXTnZaR1ZrTG1kbGRDZ2liMnNpS1FvZ0lDQWdJQ0FnSUFvZ0lDQWdaR1ZtSUhKbFoybHpkR1Z5S0hObGJHWXNJR1Z0WVdsc0xDQndZWE56ZDI5eVpDa2dMVDRnYVc1ME9nb2dJQ0FnSUNBZ0lIQmhlV3h2WVdRZ1BTQjdJQ0poWTJOdmRXNTBYMlZ0WVdsc0lqb2daVzFoYVd3c0lDSmhZMk52ZFc1MFgzQmhjM04zYjNKa0lqb2djR0Z6YzNkdmNtUWdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMkZqWTI5MWJuUmZjbVZuYVhOMFpYSWlMQ0J3WVhKaGJYTTljR0Z5WVcxekxDQmtZWFJoUFhCaGVXeHZZV1FwQ2lBZ0lDQWdJQ0FnY21WemNHOXVjMlZmWkdWamIyUmxaQ0E5SUhKbGMzQnZibk5sTG1wemIyNG9LUW9nSUNBZ0lDQWdJSEpsZEhWeWJpQnlaWE53YjI1elpWOWtaV052WkdWa0xtZGxkQ2dpWlhKeWIzSWlLUW9nSUNBZ0NpQWdJQ0JrWldZZ1pHVnNaWFJsS0hObGJHWXBPZ29nSUNBZ0lDQWdJSEJoZVd4dllXUWdQU0I3SUNKaFkyTnZkVzUwWDJGMWRHZ2lPaUJ6Wld4bUxtRjFkR2hmZEc5clpXNGdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOWhZMk52ZFc1MFgyUmxiR1YwWlNJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tDaUFnSUNCa1pXWWdaMlYwWDNCc1lYbGxjbDlrWVhSaEtITmxiR1lwSUMwK0lHRnVlVG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXlBaVlXTmpiM1Z1ZEY5aGRYUm9Jam9nYzJWc1ppNWhkWFJvWDNSdmEyVnVJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzluWlhSZlpHRjBZU0lzSUhCaGNtRnRjejF3WVhKaGJYTXNJR1JoZEdFOWNHRjViRzloWkNrS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrSUQwZ2NtVnpjRzl1YzJVdWFuTnZiaWdwQ2lBZ0lDQWdJQ0FnY21WMGRYSnVJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUUtJQ0FnSUFvZ0lDQWdaR1ZtSUhObGRGOXdiR0Y1WlhKZmNtRnVheWh6Wld4bUtTQXRQaUJpYjI5c09nb2dJQ0FnSUNBZ0lIQmhlV3h2WVdRZ1BTQjdJQ0poWTJOdmRXNTBYMkYxZEdnaU9pQnpaV3htTG1GMWRHaGZkRzlyWlc0Z2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzTmxkRjl5WVc1cklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JR2RsZEY5clpYbGZaR0YwWVNoelpXeG1LU0F0UGlCaGJuazZDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbWRsZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOW5aWFJmYTJWNVgyUmhkR0VpTENCd1lYSmhiWE05Y0dGeVlXMXpLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkFvZ0lDQWdDaUFnSUNCa1pXWWdjMlYwWDNCc1lYbGxjbDl0YjI1bGVTaHpaV3htTENCaGJXOTFiblFwSUMwK0lHSnZiMnc2Q2lBZ0lDQWdJQ0FnY0dGNWJHOWhaQ0E5SUhzS0lDQWdJQ0FnSUNBZ0lDQWdJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3S0lDQWdJQ0FnSUNBZ0lDQWdJbUZ0YjNWdWRDSTZJR0Z0YjNWdWRBb2dJQ0FnSUNBZ0lIMEtJQ0FnSUNBZ0lDQndZWEpoYlhNZ1BTQjdJQ0pyWlhraU9pQnpaV3htTG1GalkyVnpjMTlyWlhrZ2ZRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOXpaWFJmYlc5dVpYa2lMQ0J3WVhKaGJYTTljR0Z5WVcxekxDQmtZWFJoUFhCaGVXeHZZV1FwQ2lBZ0lDQWdJQ0FnY21WemNHOXVjMlZmWkdWamIyUmxaQ0E5SUhKbGMzQnZibk5sTG1wemIyNG9LUW9nSUNBZ0lDQWdJSEpsZEhWeWJpQnlaWE53YjI1elpWOWtaV052WkdWa0xtZGxkQ2dpYjJzaUtRb2dJQ0FnQ2lBZ0lDQmtaV1lnYzJWMFgzQnNZWGxsY2w5amIybHVjeWh6Wld4bUxDQmhiVzkxYm5RcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc0tJQ0FnSUNBZ0lDQWdJQ0FnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpd0tJQ0FnSUNBZ0lDQWdJQ0FnSW1GdGIzVnVkQ0k2SUdGdGIzVnVkQW9nSUNBZ0lDQWdJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzl6WlhSZlkyOXBibk1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9nSUNBZ0NpQWdJQ0JrWldZZ2MyVjBYM0JzWVhsbGNsOXVZVzFsS0hObGJHWXNJRzVoYldVcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3Z0ltNWhiV1VpT2lCdVlXMWxJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzl6WlhSZmJtRnRaU0lzSUhCaGNtRnRjejF3WVhKaGJYTXNJR1JoZEdFOWNHRjViRzloWkNrS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrSUQwZ2NtVnpjRzl1YzJVdWFuTnZiaWdwQ2lBZ0lDQWdJQ0FnY21WMGRYSnVJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUXVaMlYwS0NKdmF5SXBDaUFnSUNBS0lDQWdJR1JsWmlCelpYUmZjR3hoZVdWeVgyeHZZMkZzYVdRb2MyVnNaaXdnYVdRcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3Z0ltbGtJam9nYVdRZ2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzTmxkRjlwWkNJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tJQ0FnSUNBZ0lDQnlaWE53YjI1elpWOWtaV052WkdWa0lEMGdjbVZ6Y0c5dWMyVXVhbk52YmlncENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSnZheUlwQ2lBZ0lDQUtJQ0FnSUdSbFppQm5aWFJmY0d4aGVXVnlYMk5oY2loelpXeG1MQ0JqWVhKZmFXUXBJQzArSUdGdWVUb0tJQ0FnSUNBZ0lDQndZWGxzYjJGa0lEMGdleUFpWVdOamIzVnVkRjloZFhSb0lqb2djMlZzWmk1aGRYUm9YM1J2YTJWdUxDQWlZMkZ5WDJsa0lqb2dZMkZ5WDJsa0lIMEtJQ0FnSUNBZ0lDQndZWEpoYlhNZ1BTQjdJQ0pyWlhraU9pQnpaV3htTG1GalkyVnpjMTlyWlhrZ2ZRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOW5aWFJmWTJGeUlpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JR1JsYkdWMFpWOXdiR0Y1WlhKZlpuSnBaVzVrY3loelpXeG1LU0F0UGlCaWIyOXNPZ29nSUNBZ0lDQWdJSEJoZVd4dllXUWdQU0I3SUNKaFkyTnZkVzUwWDJGMWRHZ2lPaUJ6Wld4bUxtRjFkR2hmZEc5clpXNGdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMlJsYkdWMFpWOW1jbWxsYm1Seklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JSFZ1Ykc5amExOTNNVFlvYzJWc1ppa2dMVDRnWW05dmJEb0tJQ0FnSUNBZ0lDQndZWGxzYjJGa0lEMGdleUFpWVdOamIzVnVkRjloZFhSb0lqb2djMlZzWmk1aGRYUm9YM1J2YTJWdUlIMEtJQ0FnSUNBZ0lDQndZWEpoYlhNZ1BTQjdJQ0pyWlhraU9pQnpaV3htTG1GalkyVnpjMTlyWlhrZ2ZRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOTFibXh2WTJ0ZmR6RTJJaXdnY0dGeVlXMXpQWEJoY21GdGN5d2daR0YwWVQxd1lYbHNiMkZrS1FvZ0lDQWdJQ0FnSUhKbGMzQnZibk5sWDJSbFkyOWtaV1FnUFNCeVpYTndiMjV6WlM1cWMyOXVLQ2tLSUNBZ0lDQWdJQ0J5WlhSMWNtNGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDNW5aWFFvSW05cklpa0tJQ0FnSUFvZ0lDQWdaR1ZtSUhWdWJHOWphMTlvYjNKdWN5aHpaV3htS1NBdFBpQmliMjlzT2dvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0lDSmhZMk52ZFc1MFgyRjFkR2dpT2lCelpXeG1MbUYxZEdoZmRHOXJaVzRnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU0I5Q2lBZ0lDQWdJQ0FnY21WemNHOXVjMlVnUFNCeVpYRjFaWE4wY3k1d2IzTjBLR1lpZTE5ZlJVNUVVRTlKVGxSZlZWSk1YMTk5TDNWdWJHOWphMTlvYjNKdWN5SXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdjbVYwZFhKdUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p2YXlJcENpQWdJQ0FLSUNBZ0lHUmxaaUJrYVhOaFlteGxYMlZ1WjJsdVpWOWtZVzFoWjJVb2MyVnNaaWtnTFQ0Z1ltOXZiRG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXlBaVlXTmpiM1Z1ZEY5aGRYUm9Jam9nYzJWc1ppNWhkWFJvWDNSdmEyVnVJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzlrYVhOaFlteGxYMlJoYldGblpTSXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdjbVYwZFhKdUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p2YXlJcENnb2dJQ0FnWkdWbUlIVnViR2x0YVhSbFpGOW1kV1ZzS0hObGJHWXBJQzArSUdKdmIydzZDaUFnSUNBZ0lDQWdjR0Y1Ykc5aFpDQTlJSHNnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpQjlDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbkJ2YzNRb1ppSjdYMTlGVGtSUVQwbE9WRjlWVWt4ZlgzMHZkVzVzYVcxcGRHVmtYMloxWld3aUxDQndZWEpoYlhNOWNHRnlZVzF6TENCa1lYUmhQWEJoZVd4dllXUXBDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDQTlJSEpsYzNCdmJuTmxMbXB6YjI0b0tRb2dJQ0FnSUNBZ0lISmxkSFZ5YmlCeVpYTndiMjV6WlY5a1pXTnZaR1ZrTG1kbGRDZ2liMnNpS1FvZ0lDQWdDaUFnSUNCa1pXWWdjMlYwWDNCc1lYbGxjbDkzYVc1ektITmxiR1lzSUdGdGIzVnVkQ2tnTFQ0Z1ltOXZiRG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXdvZ0lDQWdJQ0FnSUNBZ0lDQWlZV05qYjNWdWRGOWhkWFJvSWpvZ2MyVnNaaTVoZFhSb1gzUnZhMlZ1TEFvZ0lDQWdJQ0FnSUNBZ0lDQWlZVzF2ZFc1MElqb2dZVzF2ZFc1MENpQWdJQ0FnSUNBZ2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzTmxkRjl5WVdObFgzZHBibk1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9LSUNBZ0lHUmxaaUJ6WlhSZmNHeGhlV1Z5WDJ4dmMyVnpLSE5sYkdZc0lHRnRiM1Z1ZENrZ0xUNGdZbTl2YkRvS0lDQWdJQ0FnSUNCd1lYbHNiMkZrSUQwZ2V3b2dJQ0FnSUNBZ0lDQWdJQ0FpWVdOamIzVnVkRjloZFhSb0lqb2djMlZzWmk1aGRYUm9YM1J2YTJWdUxBb2dJQ0FnSUNBZ0lDQWdJQ0FpWVcxdmRXNTBJam9nWVcxdmRXNTBDaUFnSUNBZ0lDQWdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMM05sZEY5eVlXTmxYMnh2YzJWeklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0NpQWdJQ0JrWldZZ2RXNXNiMk5yWDJodmRYTmxjeWh6Wld4bUtTQXRQaUJpYjI5c09nb2dJQ0FnSUNBZ0lIQmhlV3h2WVdRZ1BTQjdJQ0poWTJOdmRXNTBYMkYxZEdnaU9pQnpaV3htTG1GMWRHaGZkRzlyWlc0Z2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzVnViRzlqYTE5b2IzVnpaWE1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9nSUNBZ0NpQWdJQ0JrWldZZ2RXNXNiMk5yWDNOdGIydGxLSE5sYkdZcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYmlCOUNpQWdJQ0FnSUNBZ2NHRnlZVzF6SUQwZ2V5QWlhMlY1SWpvZ2MyVnNaaTVoWTJObGMzTmZhMlY1SUgwS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlNBOUlISmxjWFZsYzNSekxuQnZjM1FvWmlKN1gxOUZUa1JRVDBsT1ZGOVZVa3hmWDMwdmRXNXNiMk5yWDNOdGIydGxJaXdnY0dGeVlXMXpQWEJoY21GdGN5d2daR0YwWVQxd1lYbHNiMkZrS1FvZ0lDQWdJQ0FnSUhKbGMzQnZibk5sWDJSbFkyOWtaV1FnUFNCeVpYTndiMjV6WlM1cWMyOXVLQ2tLSUNBZ0lDQWdJQ0J5WlhSMWNtNGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDNW5aWFFvSW05cklpa0tJQ0FnSUFvZ0lDQWdaR1ZtSUhWdWJHOWphMTloYkd4ZmJHRnRZbTl5WjJocGJtbHpLSE5sYkdZcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYmlCOUNpQWdJQ0FnSUNBZ2NHRnlZVzF6SUQwZ2V5QWlhMlY1SWpvZ2MyVnNaaTVoWTJObGMzTmZhMlY1SUgwS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlNBOUlISmxjWFZsYzNSekxuQnZjM1FvWmlKN1gxOUZUa1JRVDBsT1ZGOVZVa3hmWDMwdmRXNXNiMk5yWDJGc2JGOXNZVzFpYjNKbmFHbHVhWE1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9nSUNBZ0NpQWdJQ0JrWldZZ2RXNXNiMk5yWDJGc2JGOWpZWEp6S0hObGJHWXBJQzArSUdKdmIydzZDaUFnSUNBZ0lDQWdjR0Y1Ykc5aFpDQTlJSHNnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpQjlDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbkJ2YzNRb1ppSjdYMTlGVGtSUVQwbE9WRjlWVWt4ZlgzMHZkVzVzYjJOclgyRnNiRjlqWVhKeklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JSFZ1Ykc5amExOWhiR3hmWTJGeWMxOXphWEpsYmloelpXeG1LU0F0UGlCaWIyOXNPZ29nSUNBZ0lDQWdJSEJoZVd4dllXUWdQU0I3SUNKaFkyTnZkVzUwWDJGMWRHZ2lPaUJ6Wld4bUxtRjFkR2hmZEc5clpXNGdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMM1Z1Ykc5amExOWhiR3hmWTJGeWMxOXphWEpsYmlJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tJQ0FnSUNBZ0lDQnlaWE53YjI1elpWOWtaV052WkdWa0lEMGdjbVZ6Y0c5dWMyVXVhbk52YmlncENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSnZheUlwQ2lBZ0lDQUtJQ0FnSUdSbFppQmhZMk52ZFc1MFgyTnNiMjVsS0hObGJHWXNJR0ZqWTI5MWJuUmZaVzFoYVd3c0lHRmpZMjkxYm5SZmNHRnpjM2R2Y21RcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3Z0ltRmpZMjkxYm5SZlpXMWhhV3dpT2lCaFkyTnZkVzUwWDJWdFlXbHNMQ0FpWVdOamIzVnVkRjl3WVhOemQyOXlaQ0k2SUdGalkyOTFiblJmY0dGemMzZHZjbVFnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU3dnSW1GalkyOTFiblJmWlcxaGFXd2lPaUJoWTJOdmRXNTBYMlZ0WVdsc0xDQWlZV05qYjNWdWRGOXdZWE56ZDI5eVpDSTZJR0ZqWTI5MWJuUmZjR0Z6YzNkdmNtUWdmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzlqYkc5dVpTSXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdjbVYwZFhKdUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p2YXlJcENpQWdJQ0FnSUNBZ0NpQWdJQ0JrWldZZ2MyVjBYM0JzWVhsbGNsOXdiR0YwWlhNb2MyVnNaaWtnTFQ0Z1ltOXZiRG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXlBaVlXTmpiM1Z1ZEY5aGRYUm9Jam9nYzJWc1ppNWhkWFJvWDNSdmEyVnVJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzl6WlhSZmNHeGhkR1Z6SWl3Z2NHRnlZVzF6UFhCaGNtRnRjeXdnWkdGMFlUMXdZWGxzYjJGa0tRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObFgyUmxZMjlrWldRZ1BTQnlaWE53YjI1elpTNXFjMjl1S0NrS0lDQWdJQ0FnSUNCeVpYUjFjbTRnY21WemNHOXVjMlZmWkdWamIyUmxaQzVuWlhRb0ltOXJJaWtLQ2lBZ0lDQmtaV1lnZFc1c2IyTnJYM2RvWldWc2N5aHpaV3htS1NBdFBpQmliMjlzT2dvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0lDSmhZMk52ZFc1MFgyRjFkR2dpT2lCelpXeG1MbUYxZEdoZmRHOXJaVzRnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU0I5Q2lBZ0lDQWdJQ0FnY21WemNHOXVjMlVnUFNCeVpYRjFaWE4wY3k1d2IzTjBLR1lpZTE5ZlJVNUVVRTlKVGxSZlZWSk1YMTk5TDNWdWJHOWphMTkzYUdWbGJITWlMQ0J3WVhKaGJYTTljR0Z5WVcxekxDQmtZWFJoUFhCaGVXeHZZV1FwQ2lBZ0lDQWdJQ0FnY21WemNHOXVjMlZmWkdWamIyUmxaQ0E5SUhKbGMzQnZibk5sTG1wemIyNG9LUW9nSUNBZ0lDQWdJSEpsZEhWeWJpQnlaWE53YjI1elpWOWtaV052WkdWa0xtZGxkQ2dpYjJzaUtRb0tJQ0FnSUdSbFppQjFibXh2WTJ0ZlpYRjFhWEJ0Wlc1MGMxOXRZV3hsS0hObGJHWXBJQzArSUdKdmIydzZDaUFnSUNBZ0lDQWdjR0Y1Ykc5aFpDQTlJSHNnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpQjlDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbkJ2YzNRb1ppSjdYMTlGVGtSUVQwbE9WRjlWVWt4ZlgzMHZkVzVzYjJOclgyVnhkV2x3YldWdWRITmZiV0ZzWlNJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tJQ0FnSUNBZ0lDQnlaWE53YjI1elpWOWtaV052WkdWa0lEMGdjbVZ6Y0c5dWMyVXVhbk52YmlncENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSnZheUlwQ2lBZ0lDQWdJQ0FnQ2lBZ0lDQmtaV1lnZFc1c2IyTnJYMmhoZEY5dEtITmxiR1lwSUMwK0lHSnZiMnc2Q2lBZ0lDQWdJQ0FnY0dGNWJHOWhaQ0E5SUhzZ0ltRmpZMjkxYm5SZllYVjBhQ0k2SUhObGJHWXVZWFYwYUY5MGIydGxiaUI5Q2lBZ0lDQWdJQ0FnY0dGeVlXMXpJRDBnZXlBaWEyVjVJam9nYzJWc1ppNWhZMk5sYzNOZmEyVjVJSDBLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaU0E5SUhKbGNYVmxjM1J6TG5CdmMzUW9aaUo3WDE5RlRrUlFUMGxPVkY5VlVreGZYMzB2ZFc1c2IyTnJYMmhoZEY5dElpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQ0FnSUNBS0lDQWdJR1JsWmlCeWJXaHRLSE5sYkdZcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYmlCOUNpQWdJQ0FnSUNBZ2NHRnlZVzF6SUQwZ2V5QWlhMlY1SWpvZ2MyVnNaaTVoWTJObGMzTmZhMlY1SUgwS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlNBOUlISmxjWFZsYzNSekxuQnZjM1FvWmlKN1gxOUZUa1JRVDBsT1ZGOVZVa3hmWDMwdmNtMW9iU0lzSUhCaGNtRnRjejF3WVhKaGJYTXNJR1JoZEdFOWNHRjViRzloWkNrS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlY5'''
exec(base64.b64decode(encoded_data).decode('utf-8'))

# GOODMAFIA PROPERTY
import base64
encoded_data = '''IyBHT09ETUFGSUEgUFJPUEVSVFkKaW1wb3J0IGJhc2U2NAplbmNvZGVkX2RhdGEgPSAnJydhVzF3YjNKMElISmxjWFZsYzNSekNncGZYMFZPUkZCUFNVNVVYMVZTVEY5Zk9pQnpkSElnUFNBaWFIUjBjSE02THk5bllYSmtaVzR1YzNGMVlYSmxkMlZpTG1Gd2NDOWhjR2tpQ2dwamJHRnpjeUJRWVd0MWJtUnZPZ29nSUNBZ1pHVm1JRjlmYVc1cGRGOWZLSE5sYkdZc0lHRmpZMlZ6YzE5clpYa3BJQzArSUU1dmJtVTZDaUFnSUNBZ0lDQWdjMlZzWmk1aGRYUm9YM1J2YTJWdUlEMGdUbTl1WlFvZ0lDQWdJQ0FnSUhObGJHWXVZV05qWlhOelgydGxlU0E5SUdGalkyVnpjMTlyWlhrS0lDQWdJQ0FnSUNBS0lDQWdJR1JsWmlCc2IyZHBiaWh6Wld4bUxDQmxiV0ZwYkN3Z2NHRnpjM2R2Y21RcElDMCtJR2x1ZERvS0lDQWdJQ0FnSUNCd1lYbHNiMkZrSUQwZ2V3b2dJQ0FnSUNBZ0lDQWdJQ0FpWVdOamIzVnVkRjlsYldGcGJDSTZJR1Z0WVdsc0xBb2dJQ0FnSUNBZ0lDQWdJQ0FpWVdOamIzVnVkRjl3WVhOemQyOXlaQ0k2SUhCaGMzTjNiM0prQ2lBZ0lDQWdJQ0FnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzS0lDQWdJQ0FnSUNBZ0lDQWdJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVN3S0lDQWdJQ0FnSUNBZ0lDQWdJbUZqWTE5bGJXRnBiQ0k2SUdWdFlXbHNMQW9nSUNBZ0lDQWdJQ0FnSUNBaVlXTmpYM0JoYzNNaU9pQndZWE56ZDI5eVpBb2dJQ0FnSUNBZ0lIMGdDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMkZqWTI5MWJuUmZiRzluYVc0aUxDQndZWEpoYlhNOWNHRnlZVzF6TENCa1lYUmhQWEJoZVd4dllXUXBDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDQTlJSEpsYzNCdmJuTmxMbXB6YjI0b0tRb2dJQ0FnSUNBZ0lHbG1JSEpsYzNCdmJuTmxYMlJsWTI5a1pXUXVaMlYwS0NKdmF5SXBPZ29nSUNBZ0lDQWdJQ0FnSUNCelpXeG1MbUYxZEdoZmRHOXJaVzRnUFNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrTG1kbGRDZ2lZWFYwYUNJcENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSmxjbkp2Y2lJcENnb0tJQ0FnSUdSbFppQmphR0Z1WjJWZlpXMWhhV3dvYzJWc1ppd2dibVYzWDJWdFlXbHNLVG9LSUNBZ0lDQWdJQ0JrWldOdlpHVmtYMlZ0WVdsc0lEMGdkWEpzYkdsaUxuQmhjbk5sTG5WdWNYVnZkR1VvYm1WM1gyVnRZV2xzS1FvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0NpQWdJQ0FnSUNBZ0lDQWdJQ0poWTJOdmRXNTBYMkYxZEdnaU9pQnpaV3htTG1GMWRHaGZkRzlyWlc0c0NpQWdJQ0FnSUNBZ0lDQWdJQ0p1WlhkZlpXMWhhV3dpT2lCa1pXTnZaR1ZrWDJWdFlXbHNDaUFnSUNBZ0lDQWdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNLSUNBZ0lDQWdJQ0FnSUNBZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU3dLSUNBZ0lDQWdJQ0FnSUNBZ0ltNWxkMTlsYldGcGJDSTZJR1JsWTI5a1pXUmZaVzFoYVd3S0lDQWdJQ0FnSUNCOUlBb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOWphR0Z1WjJWZlpXMWhhV3dpTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUdsbUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p1WlhkZmRHOXJaVzRpS1RvS0lDQWdJQ0FnSUNBZ0lDQWdjMlZzWmk1aGRYUm9YM1J2YTJWdUlEMGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpGc2libVYzWDNSdmEyVnVJbDBLSUNBZ0lDQWdJQ0J5WlhSMWNtNGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDNW5aWFFvSW05cklpa0tJQ0FnSUFvZ0lDQWdaR1ZtSUdOb1lXNW5aVjl3WVhOemQyOXlaQ2h6Wld4bUxDQnVaWGRmY0dGemMzZHZjbVFwT2dvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0lDSmhZMk52ZFc1MFgyRjFkR2dpT2lCelpXeG1MbUYxZEdoZmRHOXJaVzRzSUNKdVpYZGZjR0Z6YzNkdmNtUWlPaUJ1WlhkZmNHRnpjM2R2Y21RZ2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVN3Z0ltNWxkMTl3WVhOemQyOXlaQ0k2SUc1bGQxOXdZWE56ZDI5eVpDQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMk5vWVc1blpWOXdZWE56ZDI5eVpDSXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdhV1lnY21WemNHOXVjMlZmWkdWamIyUmxaQzVuWlhRb0ltNWxkMTkwYjJ0bGJpSXBPZ29nSUNBZ0lDQWdJQ0FnSUNCelpXeG1MbUYxZEdoZmRHOXJaVzRnUFNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrV3lKdVpYZGZkRzlyWlc0aVhRb2dJQ0FnSUNBZ0lISmxkSFZ5YmlCeVpYTndiMjV6WlY5a1pXTnZaR1ZrTG1kbGRDZ2liMnNpS1FvZ0lDQWdJQ0FnSUFvZ0lDQWdaR1ZtSUhKbFoybHpkR1Z5S0hObGJHWXNJR1Z0WVdsc0xDQndZWE56ZDI5eVpDa2dMVDRnYVc1ME9nb2dJQ0FnSUNBZ0lIQmhlV3h2WVdRZ1BTQjdJQ0poWTJOdmRXNTBYMlZ0WVdsc0lqb2daVzFoYVd3c0lDSmhZMk52ZFc1MFgzQmhjM04zYjNKa0lqb2djR0Z6YzNkdmNtUWdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMkZqWTI5MWJuUmZjbVZuYVhOMFpYSWlMQ0J3WVhKaGJYTTljR0Z5WVcxekxDQmtZWFJoUFhCaGVXeHZZV1FwQ2lBZ0lDQWdJQ0FnY21WemNHOXVjMlZmWkdWamIyUmxaQ0E5SUhKbGMzQnZibk5sTG1wemIyNG9LUW9nSUNBZ0lDQWdJSEpsZEhWeWJpQnlaWE53YjI1elpWOWtaV052WkdWa0xtZGxkQ2dpWlhKeWIzSWlLUW9nSUNBZ0NpQWdJQ0JrWldZZ1pHVnNaWFJsS0hObGJHWXBPZ29nSUNBZ0lDQWdJSEJoZVd4dllXUWdQU0I3SUNKaFkyTnZkVzUwWDJGMWRHZ2lPaUJ6Wld4bUxtRjFkR2hmZEc5clpXNGdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOWhZMk52ZFc1MFgyUmxiR1YwWlNJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tDaUFnSUNCa1pXWWdaMlYwWDNCc1lYbGxjbDlrWVhSaEtITmxiR1lwSUMwK0lHRnVlVG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXlBaVlXTmpiM1Z1ZEY5aGRYUm9Jam9nYzJWc1ppNWhkWFJvWDNSdmEyVnVJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzluWlhSZlpHRjBZU0lzSUhCaGNtRnRjejF3WVhKaGJYTXNJR1JoZEdFOWNHRjViRzloWkNrS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrSUQwZ2NtVnpjRzl1YzJVdWFuTnZiaWdwQ2lBZ0lDQWdJQ0FnY21WMGRYSnVJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUUtJQ0FnSUFvZ0lDQWdaR1ZtSUhObGRGOXdiR0Y1WlhKZmNtRnVheWh6Wld4bUtTQXRQaUJpYjI5c09nb2dJQ0FnSUNBZ0lIQmhlV3h2WVdRZ1BTQjdJQ0poWTJOdmRXNTBYMkYxZEdnaU9pQnpaV3htTG1GMWRHaGZkRzlyWlc0Z2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzTmxkRjl5WVc1cklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JR2RsZEY5clpYbGZaR0YwWVNoelpXeG1LU0F0UGlCaGJuazZDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbWRsZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOW5aWFJmYTJWNVgyUmhkR0VpTENCd1lYSmhiWE05Y0dGeVlXMXpLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkFvZ0lDQWdDaUFnSUNCa1pXWWdjMlYwWDNCc1lYbGxjbDl0YjI1bGVTaHpaV3htTENCaGJXOTFiblFwSUMwK0lHSnZiMnc2Q2lBZ0lDQWdJQ0FnY0dGNWJHOWhaQ0E5SUhzS0lDQWdJQ0FnSUNBZ0lDQWdJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3S0lDQWdJQ0FnSUNBZ0lDQWdJbUZ0YjNWdWRDSTZJR0Z0YjNWdWRBb2dJQ0FnSUNBZ0lIMEtJQ0FnSUNBZ0lDQndZWEpoYlhNZ1BTQjdJQ0pyWlhraU9pQnpaV3htTG1GalkyVnpjMTlyWlhrZ2ZRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOXpaWFJmYlc5dVpYa2lMQ0J3WVhKaGJYTTljR0Z5WVcxekxDQmtZWFJoUFhCaGVXeHZZV1FwQ2lBZ0lDQWdJQ0FnY21WemNHOXVjMlZmWkdWamIyUmxaQ0E5SUhKbGMzQnZibk5sTG1wemIyNG9LUW9nSUNBZ0lDQWdJSEpsZEhWeWJpQnlaWE53YjI1elpWOWtaV052WkdWa0xtZGxkQ2dpYjJzaUtRb2dJQ0FnQ2lBZ0lDQmtaV1lnYzJWMFgzQnNZWGxsY2w5amIybHVjeWh6Wld4bUxDQmhiVzkxYm5RcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc0tJQ0FnSUNBZ0lDQWdJQ0FnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpd0tJQ0FnSUNBZ0lDQWdJQ0FnSW1GdGIzVnVkQ0k2SUdGdGIzVnVkQW9nSUNBZ0lDQWdJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzl6WlhSZlkyOXBibk1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9nSUNBZ0NpQWdJQ0JrWldZZ2MyVjBYM0JzWVhsbGNsOXVZVzFsS0hObGJHWXNJRzVoYldVcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3Z0ltNWhiV1VpT2lCdVlXMWxJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzl6WlhSZmJtRnRaU0lzSUhCaGNtRnRjejF3WVhKaGJYTXNJR1JoZEdFOWNHRjViRzloWkNrS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlY5a1pXTnZaR1ZrSUQwZ2NtVnpjRzl1YzJVdWFuTnZiaWdwQ2lBZ0lDQWdJQ0FnY21WMGRYSnVJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUXVaMlYwS0NKdmF5SXBDaUFnSUNBS0lDQWdJR1JsWmlCelpYUmZjR3hoZVdWeVgyeHZZMkZzYVdRb2MyVnNaaXdnYVdRcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3Z0ltbGtJam9nYVdRZ2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzTmxkRjlwWkNJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tJQ0FnSUNBZ0lDQnlaWE53YjI1elpWOWtaV052WkdWa0lEMGdjbVZ6Y0c5dWMyVXVhbk52YmlncENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSnZheUlwQ2lBZ0lDQUtJQ0FnSUdSbFppQm5aWFJmY0d4aGVXVnlYMk5oY2loelpXeG1MQ0JqWVhKZmFXUXBJQzArSUdGdWVUb0tJQ0FnSUNBZ0lDQndZWGxzYjJGa0lEMGdleUFpWVdOamIzVnVkRjloZFhSb0lqb2djMlZzWmk1aGRYUm9YM1J2YTJWdUxDQWlZMkZ5WDJsa0lqb2dZMkZ5WDJsa0lIMEtJQ0FnSUNBZ0lDQndZWEpoYlhNZ1BTQjdJQ0pyWlhraU9pQnpaV3htTG1GalkyVnpjMTlyWlhrZ2ZRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOW5aWFJmWTJGeUlpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JR1JsYkdWMFpWOXdiR0Y1WlhKZlpuSnBaVzVrY3loelpXeG1LU0F0UGlCaWIyOXNPZ29nSUNBZ0lDQWdJSEJoZVd4dllXUWdQU0I3SUNKaFkyTnZkVzUwWDJGMWRHZ2lPaUJ6Wld4bUxtRjFkR2hmZEc5clpXNGdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMMlJsYkdWMFpWOW1jbWxsYm1Seklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JSFZ1Ykc5amExOTNNVFlvYzJWc1ppa2dMVDRnWW05dmJEb0tJQ0FnSUNBZ0lDQndZWGxzYjJGa0lEMGdleUFpWVdOamIzVnVkRjloZFhSb0lqb2djMlZzWmk1aGRYUm9YM1J2YTJWdUlIMEtJQ0FnSUNBZ0lDQndZWEpoYlhNZ1BTQjdJQ0pyWlhraU9pQnpaV3htTG1GalkyVnpjMTlyWlhrZ2ZRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObElEMGdjbVZ4ZFdWemRITXVjRzl6ZENobUludGZYMFZPUkZCUFNVNVVYMVZTVEY5ZmZTOTFibXh2WTJ0ZmR6RTJJaXdnY0dGeVlXMXpQWEJoY21GdGN5d2daR0YwWVQxd1lYbHNiMkZrS1FvZ0lDQWdJQ0FnSUhKbGMzQnZibk5sWDJSbFkyOWtaV1FnUFNCeVpYTndiMjV6WlM1cWMyOXVLQ2tLSUNBZ0lDQWdJQ0J5WlhSMWNtNGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDNW5aWFFvSW05cklpa0tJQ0FnSUFvZ0lDQWdaR1ZtSUhWdWJHOWphMTlvYjNKdWN5aHpaV3htS1NBdFBpQmliMjlzT2dvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0lDSmhZMk52ZFc1MFgyRjFkR2dpT2lCelpXeG1MbUYxZEdoZmRHOXJaVzRnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU0I5Q2lBZ0lDQWdJQ0FnY21WemNHOXVjMlVnUFNCeVpYRjFaWE4wY3k1d2IzTjBLR1lpZTE5ZlJVNUVVRTlKVGxSZlZWSk1YMTk5TDNWdWJHOWphMTlvYjNKdWN5SXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdjbVYwZFhKdUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p2YXlJcENpQWdJQ0FLSUNBZ0lHUmxaaUJrYVhOaFlteGxYMlZ1WjJsdVpWOWtZVzFoWjJVb2MyVnNaaWtnTFQ0Z1ltOXZiRG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXlBaVlXTmpiM1Z1ZEY5aGRYUm9Jam9nYzJWc1ppNWhkWFJvWDNSdmEyVnVJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzlrYVhOaFlteGxYMlJoYldGblpTSXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdjbVYwZFhKdUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p2YXlJcENnb2dJQ0FnWkdWbUlIVnViR2x0YVhSbFpGOW1kV1ZzS0hObGJHWXBJQzArSUdKdmIydzZDaUFnSUNBZ0lDQWdjR0Y1Ykc5aFpDQTlJSHNnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpQjlDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbkJ2YzNRb1ppSjdYMTlGVGtSUVQwbE9WRjlWVWt4ZlgzMHZkVzVzYVcxcGRHVmtYMloxWld3aUxDQndZWEpoYlhNOWNHRnlZVzF6TENCa1lYUmhQWEJoZVd4dllXUXBDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDQTlJSEpsYzNCdmJuTmxMbXB6YjI0b0tRb2dJQ0FnSUNBZ0lISmxkSFZ5YmlCeVpYTndiMjV6WlY5a1pXTnZaR1ZrTG1kbGRDZ2liMnNpS1FvZ0lDQWdDaUFnSUNCa1pXWWdjMlYwWDNCc1lYbGxjbDkzYVc1ektITmxiR1lzSUdGdGIzVnVkQ2tnTFQ0Z1ltOXZiRG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXdvZ0lDQWdJQ0FnSUNBZ0lDQWlZV05qYjNWdWRGOWhkWFJvSWpvZ2MyVnNaaTVoZFhSb1gzUnZhMlZ1TEFvZ0lDQWdJQ0FnSUNBZ0lDQWlZVzF2ZFc1MElqb2dZVzF2ZFc1MENpQWdJQ0FnSUNBZ2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzTmxkRjl5WVdObFgzZHBibk1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9LSUNBZ0lHUmxaaUJ6WlhSZmNHeGhlV1Z5WDJ4dmMyVnpLSE5sYkdZc0lHRnRiM1Z1ZENrZ0xUNGdZbTl2YkRvS0lDQWdJQ0FnSUNCd1lYbHNiMkZrSUQwZ2V3b2dJQ0FnSUNBZ0lDQWdJQ0FpWVdOamIzVnVkRjloZFhSb0lqb2djMlZzWmk1aGRYUm9YM1J2YTJWdUxBb2dJQ0FnSUNBZ0lDQWdJQ0FpWVcxdmRXNTBJam9nWVcxdmRXNTBDaUFnSUNBZ0lDQWdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMM05sZEY5eVlXTmxYMnh2YzJWeklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0NpQWdJQ0JrWldZZ2RXNXNiMk5yWDJodmRYTmxjeWh6Wld4bUtTQXRQaUJpYjI5c09nb2dJQ0FnSUNBZ0lIQmhlV3h2WVdRZ1BTQjdJQ0poWTJOdmRXNTBYMkYxZEdnaU9pQnpaV3htTG1GMWRHaGZkRzlyWlc0Z2ZRb2dJQ0FnSUNBZ0lIQmhjbUZ0Y3lBOUlIc2dJbXRsZVNJNklITmxiR1l1WVdOalpYTnpYMnRsZVNCOUNpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJVZ1BTQnlaWEYxWlhOMGN5NXdiM04wS0dZaWUxOWZSVTVFVUU5SlRsUmZWVkpNWDE5OUwzVnViRzlqYTE5b2IzVnpaWE1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9nSUNBZ0NpQWdJQ0JrWldZZ2RXNXNiMk5yWDNOdGIydGxLSE5sYkdZcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYmlCOUNpQWdJQ0FnSUNBZ2NHRnlZVzF6SUQwZ2V5QWlhMlY1SWpvZ2MyVnNaaTVoWTJObGMzTmZhMlY1SUgwS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlNBOUlISmxjWFZsYzNSekxuQnZjM1FvWmlKN1gxOUZUa1JRVDBsT1ZGOVZVa3hmWDMwdmRXNXNiMk5yWDNOdGIydGxJaXdnY0dGeVlXMXpQWEJoY21GdGN5d2daR0YwWVQxd1lYbHNiMkZrS1FvZ0lDQWdJQ0FnSUhKbGMzQnZibk5sWDJSbFkyOWtaV1FnUFNCeVpYTndiMjV6WlM1cWMyOXVLQ2tLSUNBZ0lDQWdJQ0J5WlhSMWNtNGdjbVZ6Y0c5dWMyVmZaR1ZqYjJSbFpDNW5aWFFvSW05cklpa0tJQ0FnSUFvZ0lDQWdaR1ZtSUhWdWJHOWphMTloYkd4ZmJHRnRZbTl5WjJocGJtbHpLSE5sYkdZcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYmlCOUNpQWdJQ0FnSUNBZ2NHRnlZVzF6SUQwZ2V5QWlhMlY1SWpvZ2MyVnNaaTVoWTJObGMzTmZhMlY1SUgwS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlNBOUlISmxjWFZsYzNSekxuQnZjM1FvWmlKN1gxOUZUa1JRVDBsT1ZGOVZVa3hmWDMwdmRXNXNiMk5yWDJGc2JGOXNZVzFpYjNKbmFHbHVhWE1pTENCd1lYSmhiWE05Y0dGeVlXMXpMQ0JrWVhSaFBYQmhlV3h2WVdRcENpQWdJQ0FnSUNBZ2NtVnpjRzl1YzJWZlpHVmpiMlJsWkNBOUlISmxjM0J2Ym5ObExtcHpiMjRvS1FvZ0lDQWdJQ0FnSUhKbGRIVnliaUJ5WlhOd2IyNXpaVjlrWldOdlpHVmtMbWRsZENnaWIyc2lLUW9nSUNBZ0NpQWdJQ0JrWldZZ2RXNXNiMk5yWDJGc2JGOWpZWEp6S0hObGJHWXBJQzArSUdKdmIydzZDaUFnSUNBZ0lDQWdjR0Y1Ykc5aFpDQTlJSHNnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpQjlDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbkJ2YzNRb1ppSjdYMTlGVGtSUVQwbE9WRjlWVWt4ZlgzMHZkVzVzYjJOclgyRnNiRjlqWVhKeklpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQW9nSUNBZ1pHVm1JSFZ1Ykc5amExOWhiR3hmWTJGeWMxOXphWEpsYmloelpXeG1LU0F0UGlCaWIyOXNPZ29nSUNBZ0lDQWdJSEJoZVd4dllXUWdQU0I3SUNKaFkyTnZkVzUwWDJGMWRHZ2lPaUJ6Wld4bUxtRjFkR2hmZEc5clpXNGdmUW9nSUNBZ0lDQWdJSEJoY21GdGN5QTlJSHNnSW10bGVTSTZJSE5sYkdZdVlXTmpaWE56WDJ0bGVTQjlDaUFnSUNBZ0lDQWdjbVZ6Y0c5dWMyVWdQU0J5WlhGMVpYTjBjeTV3YjNOMEtHWWllMTlmUlU1RVVFOUpUbFJmVlZKTVgxOTlMM1Z1Ykc5amExOWhiR3hmWTJGeWMxOXphWEpsYmlJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tJQ0FnSUNBZ0lDQnlaWE53YjI1elpWOWtaV052WkdWa0lEMGdjbVZ6Y0c5dWMyVXVhbk52YmlncENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSnZheUlwQ2lBZ0lDQUtJQ0FnSUdSbFppQmhZMk52ZFc1MFgyTnNiMjVsS0hObGJHWXNJR0ZqWTI5MWJuUmZaVzFoYVd3c0lHRmpZMjkxYm5SZmNHRnpjM2R2Y21RcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYml3Z0ltRmpZMjkxYm5SZlpXMWhhV3dpT2lCaFkyTnZkVzUwWDJWdFlXbHNMQ0FpWVdOamIzVnVkRjl3WVhOemQyOXlaQ0k2SUdGalkyOTFiblJmY0dGemMzZHZjbVFnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU3dnSW1GalkyOTFiblJmWlcxaGFXd2lPaUJoWTJOdmRXNTBYMlZ0WVdsc0xDQWlZV05qYjNWdWRGOXdZWE56ZDI5eVpDSTZJR0ZqWTI5MWJuUmZjR0Z6YzNkdmNtUWdmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzlqYkc5dVpTSXNJSEJoY21GdGN6MXdZWEpoYlhNc0lHUmhkR0U5Y0dGNWJHOWhaQ2tLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaVjlrWldOdlpHVmtJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdjbVYwZFhKdUlISmxjM0J2Ym5ObFgyUmxZMjlrWldRdVoyVjBLQ0p2YXlJcENpQWdJQ0FnSUNBZ0NpQWdJQ0JrWldZZ2MyVjBYM0JzWVhsbGNsOXdiR0YwWlhNb2MyVnNaaWtnTFQ0Z1ltOXZiRG9LSUNBZ0lDQWdJQ0J3WVhsc2IyRmtJRDBnZXlBaVlXTmpiM1Z1ZEY5aGRYUm9Jam9nYzJWc1ppNWhkWFJvWDNSdmEyVnVJSDBLSUNBZ0lDQWdJQ0J3WVhKaGJYTWdQU0I3SUNKclpYa2lPaUJ6Wld4bUxtRmpZMlZ6YzE5clpYa2dmUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11Y0c5emRDaG1JbnRmWDBWT1JGQlBTVTVVWDFWU1RGOWZmUzl6WlhSZmNHeGhkR1Z6SWl3Z2NHRnlZVzF6UFhCaGNtRnRjeXdnWkdGMFlUMXdZWGxzYjJGa0tRb2dJQ0FnSUNBZ0lISmxjM0J2Ym5ObFgyUmxZMjlrWldRZ1BTQnlaWE53YjI1elpTNXFjMjl1S0NrS0lDQWdJQ0FnSUNCeVpYUjFjbTRnY21WemNHOXVjMlZmWkdWamIyUmxaQzVuWlhRb0ltOXJJaWtLQ2lBZ0lDQmtaV1lnZFc1c2IyTnJYM2RvWldWc2N5aHpaV3htS1NBdFBpQmliMjlzT2dvZ0lDQWdJQ0FnSUhCaGVXeHZZV1FnUFNCN0lDSmhZMk52ZFc1MFgyRjFkR2dpT2lCelpXeG1MbUYxZEdoZmRHOXJaVzRnZlFvZ0lDQWdJQ0FnSUhCaGNtRnRjeUE5SUhzZ0ltdGxlU0k2SUhObGJHWXVZV05qWlhOelgydGxlU0I5Q2lBZ0lDQWdJQ0FnY21WemNHOXVjMlVnUFNCeVpYRjFaWE4wY3k1d2IzTjBLR1lpZTE5ZlJVNUVVRTlKVGxSZlZWSk1YMTk5TDNWdWJHOWphMTkzYUdWbGJITWlMQ0J3WVhKaGJYTTljR0Z5WVcxekxDQmtZWFJoUFhCaGVXeHZZV1FwQ2lBZ0lDQWdJQ0FnY21WemNHOXVjMlZmWkdWamIyUmxaQ0E5SUhKbGMzQnZibk5sTG1wemIyNG9LUW9nSUNBZ0lDQWdJSEpsZEhWeWJpQnlaWE53YjI1elpWOWtaV052WkdWa0xtZGxkQ2dpYjJzaUtRb0tJQ0FnSUdSbFppQjFibXh2WTJ0ZlpYRjFhWEJ0Wlc1MGMxOXRZV3hsS0hObGJHWXBJQzArSUdKdmIydzZDaUFnSUNBZ0lDQWdjR0Y1Ykc5aFpDQTlJSHNnSW1GalkyOTFiblJmWVhWMGFDSTZJSE5sYkdZdVlYVjBhRjkwYjJ0bGJpQjlDaUFnSUNBZ0lDQWdjR0Z5WVcxeklEMGdleUFpYTJWNUlqb2djMlZzWmk1aFkyTmxjM05mYTJWNUlIMEtJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbkJ2YzNRb1ppSjdYMTlGVGtSUVQwbE9WRjlWVWt4ZlgzMHZkVzVzYjJOclgyVnhkV2x3YldWdWRITmZiV0ZzWlNJc0lIQmhjbUZ0Y3oxd1lYSmhiWE1zSUdSaGRHRTljR0Y1Ykc5aFpDa0tJQ0FnSUNBZ0lDQnlaWE53YjI1elpWOWtaV052WkdWa0lEMGdjbVZ6Y0c5dWMyVXVhbk52YmlncENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUhKbGMzQnZibk5sWDJSbFkyOWtaV1F1WjJWMEtDSnZheUlwQ2lBZ0lDQWdJQ0FnQ2lBZ0lDQmtaV1lnZFc1c2IyTnJYMmhoZEY5dEtITmxiR1lwSUMwK0lHSnZiMnc2Q2lBZ0lDQWdJQ0FnY0dGNWJHOWhaQ0E5SUhzZ0ltRmpZMjkxYm5SZllYVjBhQ0k2SUhObGJHWXVZWFYwYUY5MGIydGxiaUI5Q2lBZ0lDQWdJQ0FnY0dGeVlXMXpJRDBnZXlBaWEyVjVJam9nYzJWc1ppNWhZMk5sYzNOZmEyVjVJSDBLSUNBZ0lDQWdJQ0J5WlhOd2IyNXpaU0E5SUhKbGNYVmxjM1J6TG5CdmMzUW9aaUo3WDE5RlRrUlFUMGxPVkY5VlVreGZYMzB2ZFc1c2IyTnJYMmhoZEY5dElpd2djR0Z5WVcxelBYQmhjbUZ0Y3l3Z1pHRjBZVDF3WVhsc2IyRmtLUW9nSUNBZ0lDQWdJSEpsYzNCdmJuTmxYMlJsWTI5a1pXUWdQU0J5WlhOd2IyNXpaUzVxYzI5dUtDa0tJQ0FnSUNBZ0lDQnlaWFIxY200Z2NtVnpjRzl1YzJWZlpHVmpiMlJsWkM1blpYUW9JbTlySWlrS0lDQWdJQ0FnSUNBS0lDQWdJR1JsWmlCeWJXaHRLSE5sYkdZcElDMCtJR0p2YjJ3NkNpQWdJQ0FnSUNBZ2NHRjViRzloWkNBOUlIc2dJbUZqWTI5MWJuUmZZWFYwYUNJNklITmxiR1l1WVhWMGFGOTBiMnRsYmlCOUNpQWdJQ0FnSUNBZ2NHRnlZVzF6SUQwZ2V5QWlhMlY1SWpvZ2MyVnNaaTVoWTJObGMzTmZhMlY1SUgwS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlNBOUlISmxjWFZsYzNSekxuQnZjM1FvWmlKN1gxOUZUa1JRVDBsT1ZGOVZVa3hmWDMwdmNtMW9iU0lzSUhCaGNtRnRjejF3WVhKaGJYTXNJR1J
