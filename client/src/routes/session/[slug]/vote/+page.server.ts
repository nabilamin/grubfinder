export async function load({params}) {
    try {
        const response = await fetch(`https://api.grubfinder.io/session/${params.slug}/restaurant`,
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

        if (response.ok)
            console.log(`Successfully retrieved session with id: ${params.slug}`);
        else
            console.log('Error: Getting session failed');

        const responseBody = await response.json();

        const sessionRestaurants = responseBody;

        if (sessionRestaurants) {
            return {sessionRestaurants};
        }
    }
    catch (error) {
        console.error('Error:', error);
    }
}