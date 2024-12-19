from LogAnalyzer.analyzeTools.filter_content import get_lines_containing_keywords, get_content_between_keywords, get_lines_bewtween_strings

test_text = '''
Ein sanfter Wind strich über die weiten Felder, 
während die letzten Strahlen der Abendsonne die Landschaft in goldenes Licht tauchten. 
In der Ferne glitzerte ein kleiner Bach,
dessen leises Plätschern sich harmonisch mit dem Zwitschern der Vögel mischte.
Auf einem nahegelegenen Hügel stand eine alte Eiche, deren knorrige Äste wie Arme in den Himmel ragten.
Sie hatte Generationen von Menschen kommen und gehen sehen, ihre Geschichten still in ihrem Holz bewahrend.
Unter der Eiche saß ein junger Mann, der ein Notizbuch auf den Knien hatte.
Er kritzelte Gedanken und Skizzen hinein, inspiriert von der friedlichen Szenerie um ihn herum.
Für ihn war dieser Ort mehr als nur ein Fleck auf der Karte. Es war ein Rückzugsort, ein Platz,
an dem die Welt leiser wurde und er seinen Träumen näherkam.
Die Nacht brach herein, und mit ihr erschienen unzählige Sterne am Himmel.
Der junge Mann blickte nach oben, fasziniert von der unendlichen Weite des Universums.
Er dachte daran, wie klein und gleichzeitig bedeutungsvoll jedes Leben auf dieser Erde war.
Mit einem zufriedenen Lächeln schloss er sein Notizbuch und machte sich auf den Heimweg,
begleitet vom sanften Licht des Mondes.
Er dachte haeufig daran, wie groß und gleichzeitig geheimnisvoll jedes Leben auf dieser Erde war.

'''

test_log = '''
2024-12-19 10:00:01 INFO  MainApp - Starting application...
2024-12-19 10:00:02 DEBUG ConfigLoader - Loading configuration from file: config.properties
2024-12-19 10:00:03 INFO  DatabaseConnector - Connecting to database at jdbc:mysql://localhost:3306/appdb
2024-12-19 10:00:04 DEBUG DatabaseConnector - Connection established successfully.
2024-12-19 10:00:05 INFO  UserService - Fetching user with ID: 12345
2024-12-19 10:00:06 WARN  CacheManager - Cache miss for key: user_12345
2024-12-19 10:00:07 DEBUG DatabaseQuery - Executing query: SELECT * FROM users WHERE id = 12345
2024-12-19 10:00:08 INFO  UserService - User fetched successfully: John Doe
2024-12-19 10:00:09 ERROR FileUploader - Failed to upload file: FileNotFoundException: file.txt not found
2024-12-19 10:00:10 DEBUG RetryHandler - Retrying operation: Upload file (Attempt 1 of 3)
2024-12-19 10:00:11 INFO  FileUploader - File uploaded successfully: file.txt
2024-12-19 10:00:12 INFO  NotificationService - Sending email to: john.doe@example.com
2024-12-19 10:00:13 DEBUG EmailClient - Connecting to SMTP server: smtp.example.com
2024-12-19 10:00:14 DEBUG EmailClient - Email sent successfully to: john.doe@example.com
2024-12-19 10:00:15 WARN  AuthService - Unsuccessful login attempt for user: jane.doe@example.com
2024-12-19 10:00:16 INFO  AuthService - Login successful for user: admin@example.com
2024-12-19 10:00:17 DEBUG SessionManager - Created session for user: admin@example.com
2024-12-19 10:00:18 INFO  MainApp - Application running smoothly.
2024-12-19 10:00:19 ERROR ReportGenerator - Failed to generate report: NullPointerException
2024-12-19 10:00:20 INFO  MainApp - Shutting down application...
'''

test_string_1 = '''10:00:04 DEBUG DatabaseConnector - Connection established successfully.
2024-12-19 10:00:05 INFO  UserService - Fetching user with ID: 12345
2024-12-19 10:00:06 WARN  CacheManager - Cache miss for key: user_12345
2024-12-19 10:00:07'''

test_lines_bewtween_strings_1 = [
    "2024-12-19 10:00:07 DEBUG DatabaseQuery - Executing query: SELECT * FROM users WHERE id = 12345",
    "2024-12-19 10:00:08 INFO  UserService - User fetched successfully: John Doe",
    "2024-12-19 10:00:09 ERROR FileUploader - Failed to upload file: FileNotFoundException: file.txt not found"
    ]



def test_get_lines_containing_keywords_single_match():
    assert get_lines_containing_keywords(test_text, "Bach") == [
        "In der Ferne glitzerte ein kleiner Bach,"
        ]
    assert get_lines_containing_keywords(test_text, ["Skizzen"]) == [
        "Er kritzelte Gedanken und Skizzen hinein, inspiriert von der friedlichen Szenerie um ihn herum."
        ]
    
def test_get_lines_containing_keywords_no_match():
    assert get_lines_containing_keywords(test_text, "Napfkuchen") == []

def test_get_lines_containing_keywords_multy_kwords_single_match():
    assert get_lines_containing_keywords(test_text, ["Eiche", "Hügel"]) == [
        "Auf einem nahegelegenen Hügel stand eine alte Eiche, deren knorrige Äste wie Arme in den Himmel ragten."
    ]

def test_get_lines_containing_keywords_two_matches():
    assert get_lines_containing_keywords(test_text, ["Mann"]) == [
        "Unter der Eiche saß ein junger Mann, der ein Notizbuch auf den Knien hatte.",
        "Der junge Mann blickte nach oben, fasziniert von der unendlichen Weite des Universums."
    ]
    
def test_get_test_get_lines_containing_keywords_two_kwords_two_matches():
    assert get_lines_containing_keywords(test_text, ["Er", "Leben"]) == [
        "Er dachte daran, wie klein und gleichzeitig bedeutungsvoll jedes Leben auf dieser Erde war.",
        "Er dachte haeufig daran, wie groß und gleichzeitig geheimnisvoll jedes Leben auf dieser Erde war."
    ]
    
def test_get_lines_containing_keywords_number():
    assert get_lines_containing_keywords(test_log, ["10:00:04"]) == [
        "2024-12-19 10:00:04 DEBUG DatabaseConnector - Connection established successfully."
    ]

def test_get_content_between_keywords_single_match():
    assert get_content_between_keywords(test_log, "10:00:04", "10:00:07") == test_string_1

def test_get_lines_bewtween_strings_date():
    assert get_lines_bewtween_strings(test_log, "2024-12-19 10:00:07", "2024-12-19 10:00:09") == test_lines_bewtween_strings_1

def test_get_lines_bewtween_strings_time():
    assert get_lines_bewtween_strings(test_log, "10:00:07", "10:00:09") == test_lines_bewtween_strings_1
    
    
def test_get_full_sentence_containing_string():
    pass

def test_get_full_log_entry_containing_string():
    pass