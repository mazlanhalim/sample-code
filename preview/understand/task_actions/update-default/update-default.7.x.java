// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.rest.preview.understand.assistant.task.TaskActions;

import java.util.HashMap;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        TaskActions taskActions = TaskActions.updater(
                "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .setActions(new HashMap<String, Object>()).update();

        System.out.println(taskActions.getAssistantSid());
    }
}