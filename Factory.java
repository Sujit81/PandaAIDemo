logging.service=dev  # Change this to "prod" for production logging


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

public interface LoggingService {
    void log(String message);
}

import org.springframework.stereotype.Component;

@Component("devLoggingService")
public class DevLoggingService implements LoggingService {
    @Override
    public void log(String message) {
        System.out.println("[DEV] Logging: " + message);
    }
}


import org.springframework.stereotype.Component;

@Component("prodLoggingService")
public class ProdLoggingService implements LoggingService {
    @Override
    public void log(String message) {
        // Simulate logging to a file or external system in production
        System.out.println("[PROD] Logging: " + message);
    }
}


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class ApplicationLogger {

    private final LoggingService loggingService;

    @Autowired
    public ApplicationLogger(@Qualifier("devLoggingService") LoggingService devLoggingService,
                             @Qualifier("prodLoggingService") LoggingService prodLoggingService,
                             @Value("${logging.service}") String loggingServiceType) {

        // Conditionally choose which service to inject
        if ("prod".equalsIgnoreCase(loggingServiceType)) {
            this.loggingService = prodLoggingService;
        } else {
            this.loggingService = devLoggingService;
        }
    }

    public void logMessage(String message) {
        loggingService.log(message);
    }
}


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApp implements CommandLineRunner {

    @Autowired
    private ApplicationLogger applicationLogger;

    public static void main(String[] args) {
        SpringApplication.run(MyApp.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        // Log messages using the injected logging service
        applicationLogger.logMessage("This is a test log message.");
    }
}



