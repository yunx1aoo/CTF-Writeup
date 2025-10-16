# Pico Bank

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/65d20654-8da6-4500-aa6f-a6713cad5087" />

**Tag:** `Reverse Engineering`

**Description:** 
> In a bustling city where innovation meets finance, Pico Bank has emerged as a beacon of cutting-edge security. Promising state-of-the-art protection for your assets, the bank claims its mobile application is impervious to all forms of cyber threats. Pico Bank’s tagline, "Security Beyond the Limits," echoes through its high-tech marketing campaigns, assuring users of their utmost safety. As a cybersecurity enthusiast, your mission is to test these bold claims. You’ve been hired by a secretive organization to put Pico Bank’s mobile app through a rigorous security assessment. The flag might be in one or more locations, and additional information reveals that a Pico Bank user’s credentials were leaked in an unusual way. Your task is to crack the username and password based on the following profile information: His name is Alex Johnson with the email johnson@picobank.com, Date of Birth: March 14, 1990, Last Transaction Amount: $345.67, Pet name: tricky, and Favorite Color: Blue. To perform this challenge, you can use any Android emulator. Some examples include Genymotion Android Emulator or Android Studio. Access the Pico Bank Website Pico Bank Website and download the application.

**Attachments:** `http://saffron-estate.picoctf.net:65480/`

**Hints:**

<details>
<summary>Hint 1</summary>

Use tools like JadxGUI or apktool to inspect the APK.

</details>

<details>
<summary>Hint 2</summary>
  
Look at the app's network requests, especially for login and OTP.

</details>

<details>
<summary>Hint 3</summary>
  
The flag has two parts.

</details>

<details>
<summary>Hint 4</summary>
  
Check the server’s response after entering the correct OTP.

</details>

<details>
<summary>Hint 5</summary>

Investigate the transaction history for unusual data.

</details>

**Author:** Prince Niyonshuti N.

**Solved:** `228 users solved`

---

# Solution

<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/2a95329d-606c-4e17-8e78-1059eea1c688" />

we are given a web instance to download an application. Let's download the application and read the program code using jadx. and we check the source code of this program

<img width="150" height="200" alt="image" src="https://github.com/user-attachments/assets/52a73799-f2c2-4f87-b60b-5134491cdcd3" />

Among all these codes, there are three that are interesting in my eyes: OTP, Login, and the main activity.Let's see the contents of the login first

```java
public class Login extends AppCompatActivity {
    private Button loginButton;
    private EditText passwordEditText;
    private EditText usernameEditText;

    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_login);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), new OnApplyWindowInsetsListener() { // from class: com.example.picobank.Login$$ExternalSyntheticLambda0
            @Override // androidx.core.view.OnApplyWindowInsetsListener
            public final WindowInsetsCompat onApplyWindowInsets(View view, WindowInsetsCompat windowInsetsCompat) {
                return Login.lambda$onCreate$0(view, windowInsetsCompat);
            }
        });
        this.usernameEditText = (EditText) findViewById(R.id.username);
        this.passwordEditText = (EditText) findViewById(R.id.password);
        this.loginButton = (Button) findViewById(R.id.loginBtn);
        this.loginButton.setOnClickListener(new View.OnClickListener() { // from class: com.example.picobank.Login.1
            @Override // android.view.View.OnClickListener
            public void onClick(View v) {
                String username = Login.this.usernameEditText.getText().toString();
                String password = Login.this.passwordEditText.getText().toString();
                if ("johnson".equals(username) && "tricky1990".equals(password)) {
                    Intent intent = new Intent(Login.this, (Class<?>) OTP.class);
                    Login.this.startActivity(intent);
                    Login.this.finish();
                    return;
                }
                Toast.makeText(Login.this, "Incorrect credentials", 0).show();
            }
        });
    }
```

This means that this application has a login where there is a username and password in the code. It seems that's all that's interesting in the login section. Next, we'll check the main activity section.

```java
 protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), new OnApplyWindowInsetsListener() { // from class: com.example.picobank.MainActivity$$ExternalSyntheticLambda0
            @Override // androidx.core.view.OnApplyWindowInsetsListener
            public final WindowInsetsCompat onApplyWindowInsets(View view, WindowInsetsCompat windowInsetsCompat) {
                return MainActivity.lambda$onCreate$0(view, windowInsetsCompat);
            }
        });
        Toast.makeText(this, "Have you analyzed the server's response when handling OTP requests?", 1).show();
        this.notificationList = findViewById(R.id.notifications);
        this.notificationList.setOnClickListener(new View.OnClickListener() { // from class: com.example.picobank.MainActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, (Class<?>) Notification.class);
                MainActivity.this.startActivity(intent);
                MainActivity.this.finish();
            }
        });
        TextView welcomeMessage = (TextView) findViewById(R.id.welcomeMessage);
        welcomeMessage.setText("Welcome, Johnson");
        TextView myBalanceAmount = (TextView) findViewById(R.id.myBalanceAmount);
        myBalanceAmount.setText("$ 50,000,000");
        this.transactionsRecyclerView = (RecyclerView) findViewById(R.id.transactionsRecyclerView);
        this.transactionsRecyclerView.setLayoutManager(new LinearLayoutManager(this));
        this.transactionList = new ArrayList();
        this.transactionList.add(new Transaction("Grocery Shopping", "2023-07-21", "$ 1110000", false));
        this.transactionList.add(new Transaction("Electricity Bill", "2023-07-20", "$ 1101001", false));
        this.transactionList.add(new Transaction("Salary", "2023-07-18", "$ 1100011", true));
        this.transactionList.add(new Transaction("Internet Bill", "2023-07-17", "$ 1101111", false));
        this.transactionList.add(new Transaction("Freelance Payment", "2023-07-16", "$ 1000011", true));
        this.transactionList.add(new Transaction("Dining Out", "2023-07-15", "$ 1010100", false));
        this.transactionList.add(new Transaction("Gym Membership", "2023-07-14", "$ 1000110", false));
        this.transactionList.add(new Transaction("Stocks Dividend", "2023-07-13", "$ 1111011", true));
        this.transactionList.add(new Transaction("Car Maintenance", "2023-07-12", "$ 110001", false));
        this.transactionList.add(new Transaction("Gift Received", "2023-07-11", "$ 1011111", true));
        this.transactionList.add(new Transaction("Rent", "2023-07-10", "$ 1101100", false));
        this.transactionList.add(new Transaction("Water Bill", "2023-07-09", "$ 110001", false));
        this.transactionList.add(new Transaction("Interest Earned", "2023-07-08", "$ 110011", true));
        this.transactionList.add(new Transaction("Medical Expenses", "2023-07-07", "$ 1100100", false));
        this.transactionList.add(new Transaction("Transport", "2023-07-06", "$ 1011111", false));
        this.transactionList.add(new Transaction("Bonus", "2023-07-05", "$ 110100", true));
        this.transactionList.add(new Transaction("Subscription Service", "2023-07-04", "$ 1100010", false));
        this.transactionList.add(new Transaction("Freelance Payment", "2023-07-03", "$ 110000", true));
        this.transactionList.add(new Transaction("Entertainment", "2023-07-02", "$ 1110101", false));
        this.transactionList.add(new Transaction("Groceries", "2023-07-01", "$ 1110100", false));
        this.transactionList.add(new Transaction("Insurance Premium", "2023-06-28", "$ 1011111", false));
        this.transactionList.add(new Transaction("Charity Donation", "2023-06-26", "$ 1100010", true));
        this.transactionList.add(new Transaction("Vacation Expense", "2023-06-26", "$ 110011", false));
        this.transactionList.add(new Transaction("Home Repairs", "2023-06-24", "$ 110001", false));
        this.transactionList.add(new Transaction("Pet Care", "2023-06-22", "$ 1101110", false));
        this.transactionList.add(new Transaction("Personal Loan", "2023-06-18", "$ 1100111", true));
        this.transactionList.add(new Transaction("Childcare", "2023-06-15", "$ 1011111", false));
        this.transactionAdapter = new TransactionAdapter(this.transactionList);
        this.transactionsRecyclerView.setAdapter(this.transactionAdapter);
    }
```

Wow, in the main activity I found this interesting section. It looks like there are some binary numbers there. I'll try to make a script and convert those binary numbers to plaintext.

```python
 zsh > python
Python 3.13.7 (main, Aug 20 2025, 22:17:40) [GCC 14.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from yunxiao import *
>>> data = [
... '1110000', '1101001', '1100011', '1101111', '1000011', '1010100', '1000110',
... '1111011', '110001', '1011111', '1101100', '110001', '110011', '1100100',
... '1011111', '110100', '1100010', '110000', '1110101', '1110100', '1011111',
... '1100010', '110011', '110001', '1101110', '1100111', '1011111'
... ]
>>> print(binToText(data))
picoCTF{1_l13d_4b0ut_b31ng_
```

# FLAGPART1: picoCTF{1_l13d_4b0ut_b31ng_

After getting the first part of the flag, we still have to find the second part. because there is nothing interesting in the main activity, let's move on to OTP

```java
  protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_otp);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), new OnApplyWindowInsetsListener() { // from class: com.example.picobank.OTP$$ExternalSyntheticLambda0
            @Override // androidx.core.view.OnApplyWindowInsetsListener
            public final WindowInsetsCompat onApplyWindowInsets(View view, WindowInsetsCompat windowInsetsCompat) {
                return OTP.lambda$onCreate$0(view, windowInsetsCompat);
            }
        });
        this.otpDigit1 = (EditText) findViewById(R.id.otpDigit1);
        this.otpDigit2 = (EditText) findViewById(R.id.otpDigit2);
        this.otpDigit3 = (EditText) findViewById(R.id.otpDigit3);
        this.otpDigit4 = (EditText) findViewById(R.id.otpDigit4);
        this.submitOtpButton = (Button) findViewById(R.id.submitOtpButton);
        this.requestQueue = Volley.newRequestQueue(this);
        this.submitOtpButton.setOnClickListener(new View.OnClickListener() { // from class: com.example.picobank.OTP.1
            @Override // android.view.View.OnClickListener
            public void onClick(View v) throws JSONException {
                String otp = OTP.this.otpDigit1.getText().toString() + OTP.this.otpDigit2.getText().toString() + OTP.this.otpDigit3.getText().toString() + OTP.this.otpDigit4.getText().toString();
                OTP.this.verifyOtp(otp);
            }
        });
    }
```

In OTP, I found some interesting features. Let's start with that. It can be seen that the OTP is a 4-digit number. It seems that the application provides a text editor to enter the OTP code. Next the most interesting code is this

```java
public void verifyOtp(String otp) throws JSONException {
        String endpoint = "your server url/verify-otp";
        if (getResources().getString(R.string.otp_value).equals(otp)) {
            Intent intent = new Intent(this, (Class<?>) MainActivity.class);
            startActivity(intent);
            finish();
        } else {
            Toast.makeText(this, "Invalid OTP", 0).show();
        }
        JSONObject postData = new JSONObject();
        try {
            postData.put("otp", otp);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(1, endpoint, postData, new Response.Listener<JSONObject>() { // from class: com.example.picobank.OTP.2
            @Override // com.android.volley.Response.Listener
            public void onResponse(JSONObject response) throws JSONException {
                try {
                    boolean success = response.getBoolean("success");
                    if (success) {
                        String flag = response.getString("flag");
                        String hint = response.getString("hint");
                        Intent intent2 = new Intent(OTP.this, (Class<?>) MainActivity.class);
                        intent2.putExtra("flag", flag);
                        intent2.putExtra("hint", hint);
                        OTP.this.startActivity(intent2);
                        OTP.this.finish();
                    } else {
                        Toast.makeText(OTP.this, "Invalid OTP", 0).show();
                    }
                } catch (JSONException e2) {
                    e2.printStackTrace();
                }
            }
        }, new Response.ErrorListener() { // from class: com.example.picobank.OTP.3
            @Override // com.android.volley.Response.ErrorListener
            public void onErrorResponse(VolleyError error) {
            }
        });
        this.requestQueue.add(jsonObjectRequest);
    }
```

It's a function to verify the OTP code. There's an endpoint called /verify-otp that we use on the web instance provided to download the application. But the problem is, where is the OTP located? Next, as usual, I searched everywhere using the find feature in the GUI. I used the keyword `otp`

<img width="300" height="80" alt="image" src="https://github.com/user-attachments/assets/043d3db7-6839-4541-8bb8-31bb9fd9fbde" />

I found a variable initialization using the name `otp_value`. Let's try searching using that keyword.

<img width="1000" height="67" alt="image" src="https://github.com/user-attachments/assets/772c742c-aaa4-4c41-a7d5-9d510e547a6f" />

and yes i got the otp which is 9673 next let's send a request to the web using the endpoint /verify-otp and enter the code using json format.because I'm bored of using curl 🗿. let's just use the thunder client hhe which is in vscode. you can also use postman and so on

<img width="500" height="110" alt="image" src="https://github.com/user-attachments/assets/67c2a7a2-2d1d-4a09-b157-1e7c2d8d5dfa" />

Use post to send request to the web and don't forget to use the endpoint in the source code.

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/cc77c50b-ccd4-428a-a54f-2bab3d3ce54e" />

then add a new header Content-Type: application/json. and move to the body section

<img width="723" height="271" alt="image" src="https://github.com/user-attachments/assets/4836e6cb-4580-4eaa-86c9-549237ab0192" />

```json
{
  "otp":"9673"
}
```
add content like that. and send the request. then get the second part

<img width="1000" height="427" alt="image" src="https://github.com/user-attachments/assets/389c0ba3-b0eb-454d-ae1b-21efdd09088c" />

<br>

```json
{
  "success": true,
  "message": "OTP verified successfully",
  "flag": "s3cur3d_m0b1l3_l0g1n_c0085c75}",
  "hint": "The other part of the flag is hidden in the app"
}
```

# FLAGPART2: s3cur3d_m0b1l3_l0g1n_c0085c75}

---

# FINALFLAG: picoCTF{1_l13d_4b0ut_b31ng_s3cur3d_m0b1l3_l0g1n_c0085c75}
