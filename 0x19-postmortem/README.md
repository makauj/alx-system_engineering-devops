# Postmortem Report

## Issue Summary

- **Duration of the Outage**:  
  **Start**: February 25, 2025, 10:00 AM  
  **End**: February 25, 2025, 10:30 AM  
  **Total Duration**: 30 minutes

- **Impact**:  
  The issue caused a **500 Internal Server Error** on a WordPress website hosted on Apache, rendering the site **unavailable** to users. Approximately **100% of users** were affected, as the website was completely inaccessible during the downtime.

- **Root Cause**:  
  The root cause of the outage was a **typo in the `wp-settings.php` file**, where the filename `class-wplocale.phpp` was incorrectly specified instead of `class-wp-locale.php`. This prevented Apache from properly loading the WordPress configuration, resulting in a 500 Internal Server Error.

---

## Timeline

- **10:00 AM** - **Issue Detected**:  
  Monitoring systems detected a **500 Internal Server Error** on the WordPress website. The alert was triggered by Apache logs indicating that the site was returning errors for all users.

- **10:05 AM** - **Investigation Begins**:  
  An engineer was alerted and began investigating the issue. Initial checks revealed that the website was throwing errors related to WordPress settings, but the cause wasn’t immediately clear.

- **10:10 AM** - **Assumed Root Cause**:  
  The engineer suspected that a configuration or server-related issue might be causing the problem. Investigation included checking the Apache error logs and confirming the site’s directory permissions.

- **10:15 AM** - **Misleading Investigation**:  
  The investigation focused initially on potential Apache misconfigurations, missing PHP extensions, and database connection issues, which led to no immediate resolution.

- **10:20 AM** - **Escalation to WordPress Specialist**:  
  At this point, the engineer escalated the issue to a WordPress specialist. After a quick review of the WordPress configuration files, the typo in the `wp-settings.php` file was identified as the root cause.

- **10:25 AM** - **Issue Resolved**:  
  A Puppet script was executed to correct the typo in `wp-settings.php`, and Apache was restarted to apply the fix. The website was accessible again shortly after.

- **10:30 AM** - **Service Restored**:  
  The website was fully restored, and all users could access the site without issues.

---

## Root Cause and Resolution

- **Root Cause**:  
  The WordPress website was experiencing a 500 Internal Server Error due to a typo in the `wp-settings.php` file, where `class-wplocale.phpp` was incorrectly specified instead of the correct `class-wp-locale.php`. This caused Apache to fail when loading the WordPress configuration file.

- **Resolution**:  
  The typo was corrected using a Puppet script, which replaced `class-wplocale.phpp` with `class-wp-locale.php` in the `wp-settings.php` file. Apache was then restarted to apply the changes, resolving the 500 error and restoring website functionality.

---

## Corrective and Preventative Measures

- **Improvements and Fixes**:
  - Improve configuration review processes to catch typos or other misconfigurations before they go live.
  - Implement pre-deployment checks and unit tests for configuration files to detect any anomalies or errors in code or settings.
  - Increase visibility into WordPress configuration files through automated checks and monitoring.

- **Specific Tasks to Address the Issue**:
  1. **Puppet/Configuration Management**: Ensure that all WordPress configuration files are managed through automated tools like Puppet, which can help prevent issues due to manual errors.
  2. **Testing**: Implement unit testing for configuration files in the CI/CD pipeline to automatically detect syntax errors or incorrect paths.
  3. **Monitoring**: Set up specific alerts to monitor for 500 errors or other common WordPress errors.
  4. **Documentation**: Create and maintain a checklist for WordPress configuration that can be used to prevent issues during deployments or updates.
  5. **Knowledge Sharing**: Ensure that engineers are aware of common issues in WordPress deployments, such as configuration typos, and have quick access to resources for resolution.

By following these corrective actions, the team can reduce the likelihood of similar incidents occurring in the future, ensuring better reliability and stability for WordPress websites.
