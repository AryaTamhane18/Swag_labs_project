import os
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
from variables import PROJECT_ROOT, DATETIME

# Define directories for logging, videos, and screenshots
TMP_DIR = PROJECT_ROOT / f"tmp_{DATETIME}"
VID_DIR = TMP_DIR / "video"
SCREENSHOT_DIR = TMP_DIR / "screenshots"

# Ensure directories are created
os.makedirs(TMP_DIR, exist_ok=True)
os.makedirs(VID_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def setup_browser(context, playwright):
    """Set up the browser with appropriate configurations for testing."""

    if context.browser_name in ["msedge", "chromium"]:
        browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    elif context.browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False, slow_mo=1500)
    elif context.browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False, slow_mo=1500)
    else:
        raise ValueError("Unsupported browser type")

    context.browser_context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(VID_DIR),
        record_video_size={"width": 1280, "height": 720}
    )
    context.page = context.browser_context.new_page()
    context.browser_context.tracing.start(
        screenshots=True, snapshots=True, sources=True
    )
    return browser, context.page


def before_all(context):
    print("before all")
    """Run once at the start of test execution."""
    context.browser_name = "chromium"


@fixture
def setup_playwright(context, storage_state=False):
    """Fixture to setup the playwright before test execution.

    :param context: context object
    :type context: behave.runner.Context
    :param storage_state: User storage state for login
    :type storage_state: bool
    """
    # -- SETUP-FIXTURE PART:
    playwright = sync_playwright().start()
    browser, context.page = setup_browser(context, playwright)
    yield context.page
    # -- CLEANUP-FIXTURE PART:
    browser.close()
    playwright.stop()


def before_scenario(context, scenario):
    """Initialize the page and navigate to the Swag Labs login page before each scenario."""
    use_fixture(setup_playwright, context)
    if 'SwagLabs_login' in scenario.tags:
        print("I am in swaglabs login")
        context.page.goto("https://www.saucedemo.com/v1/")
    elif 'SwagLabs_cart' in scenario.tags:
        print("I am in swaglabs cart")
        context.page.goto("https://www.saucedemo.com/v1/inventory.html")


def after_scenario(context, scenario):
    """Attach logs, save videos, and cleanup after each scenario."""
    screenshot_path = SCREENSHOT_DIR / f"{scenario.name.replace(' ', '_')}.png"
    context.page.screenshot(path=str(screenshot_path))

    # Optionally attach the screenshot to Allure reports if used
    attach.file(str(screenshot_path), name=f"{scenario.name} Screenshot", attachment_type=AttachmentType.PNG)

    # if scenario.status == "failed":
    # Stop tracing and save trace file
    trace_path = TMP_DIR / "trace.zip"
    context.browser_context.tracing.stop(path=trace_path)
    attach.file(trace_path, name="Trace viewer logs", extension=".zip")

    # for saving vedio to allure report
    context.page.close()
    context.page.video.save_as(os.path.join(f"{VID_DIR}/{scenario.name}"))
    print(os.path.join(f"{VID_DIR}/{scenario.name}.webm"))
    with open(
            os.path.join(PROJECT_ROOT, context.page.video.path()), "rb"
    ) as video_file:
        # Video
        attach(
            video_file.read(),
            name=f"Video : {scenario.name}",
            attachment_type=AttachmentType.WEBM, )

# def after_all(context):
#     context.page.close()
#     context.browser_context.close()
#     context.browser.close()
def after_all(context):
    print("I am in after all")
