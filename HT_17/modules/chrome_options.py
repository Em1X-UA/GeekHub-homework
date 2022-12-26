# https://peter.sh/experiments/chromium-command-line-switches/

launch_options = [
            '--no-sandbox',
            '--disable-web-security',
            '--allow-running-insecure-content',
            '--hide-scrollbars',
            '--disable-setuid-sandbox',
            '--profile-directory=Default',
            '--ignore-ssl-errors=true',
            '--disable-dev-shm-usage'
        ]

non_automation = 'excludeSwitches', ['enable-automation']
disable_notifications = 'prefs', {
    'profile.default_content_setting_values.notifications': 2,
    'profile.default_content_settings.popups': 0
}
