# template when making new db
from bio.models import SocialPlatform


platforms = [
            {
        'baseUrl': '',
        'platform': 'Discord',
        'faClass': 'fa-discord',
        'isCopy':True
    },
        {
        'baseUrl': 'https://www.instagram.com/',
        'platform': 'Instagram',
        'faClass': 'fa-instagram',
    },
        {
        'baseUrl': '',
        'platform': 'spotify',
        'faClass': 'fa-spotify',
    },
    {
        'baseUrl': 'https://www.youtube.com/@',
        'platform': 'YouTube',
        'faClass': 'fa-youtube',
    },
    {
        'baseUrl': 'https://github.com/',
        'platform': 'GitHub',
        'faClass': 'fa-github',
    },
    {
        'baseUrl': 'https://twitter.com/',
        'platform': 'Twitter',
        'faClass': 'fa-twitter',
    },
    {
        'baseUrl': 'https://www.snapchat.com/add/',
        'platform': 'Snapchat',
        'faClass': 'fa-snapchat',
    },
    {
        'baseUrl': 'https://t.me/',
        'platform': 'Telegram',
        'faClass': 'fa-telegram',
    },
    {
        'baseUrl': 'https://soundcloud.com/',
        'platform': 'SoundCloud',
        'faClass': 'fa-soundcloud',
    },
    {
        'baseUrl': 'https://www.reddit.com/user/',
        'platform': 'Reddit',
        'faClass': 'fa-reddit',
    },
    {
        'baseUrl': 'https://www.twitch.tv/',
        'platform': 'Twitch',
        'faClass': 'fa-twitch',
    },
    {
        'baseUrl': 'https://www.tiktok.com/@',
        'platform': 'TikTok',
        'faClass': 'fa-tiktok',
    },
        {
        'baseUrl': 'https://www.codepen.io/',
        'platform': 'CodePen',
        'faClass': 'fa-codepen',
    },
            {
        'baseUrl': 'https://www.paypal.com/',
        'platform': 'PayPal',
        'faClass': 'fa-paypal',
    },
                {
        'baseUrl': 'https://www.vimeo.com/',
        'platform': 'Vimeo',
        'faClass': 'fa-vimeo',
    },
                    {
        'baseUrl': 'https://www.patreon.com/',
        'platform': 'Vimeo',
        'faClass': 'fa-vimeo',
    },
                        {
        'baseUrl': '',
        'platform': 'Ethereum',
        'faClass': 'fa-ethereum',
        'isCopy':True

    },
]
for platform_data in platforms:
    platform = SocialPlatform.objects.create(**platform_data)
    print(f"Added {platform.platform} platform.")
