// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE = 'ZeroBlue - where your data goes to work';
export const SITE_DESCRIPTION = 'We create custom, well-architected FileMaker solutions tailored to your business processes. Expert FileMaker development, hosting, and web development services.';
export const PAGE_SIZE = 10

const buyHoursUrl = import.meta.env.PUBLIC_STRIPE_BUY_HOURS_URL;

if (!buyHoursUrl) {
	throw new Error('PUBLIC_STRIPE_BUY_HOURS_URL is required for Buy Hours links.');
}

export const BUY_HOURS_URL = buyHoursUrl;
