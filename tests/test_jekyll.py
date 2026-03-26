import os
import yaml
from divisor.jekyll import JekyllSite
from divisor.config import Config, SiteMetadata, ContentMapping

def test_jekyll_config_creation(tmp_path):
    site_path = str(tmp_path / "site")
    config = Config(
        site_metadata=SiteMetadata(
            title="My Awesome Site: with colon",
            description="My description",
            theme="minima",
            github_repository_url="git@github.com:foo/bar.git",
            github_pages_url="https://foo.github.io/bar/",
            custom_domain="<none>"
        ),
        source_repository="some_repo",
        content_mapping=ContentMapping(
            home_page_source="home.md",
            destination_folder="site_contents",
            media_destination_folder="assets/media"
        )
    )

    jekyll_site = JekyllSite(site_path, config)
    jekyll_site.create_structure()

    config_file = os.path.join(site_path, "_config.yml")
    assert os.path.exists(config_file)

    with open(config_file, 'r') as f:
        data = yaml.safe_load(f)

    assert data['title'] == "My Awesome Site: with colon"
    assert data['description'] == "My description"
    assert data['theme'] == "minima"
    assert data['url'] == "https://foo.github.io/bar/"
