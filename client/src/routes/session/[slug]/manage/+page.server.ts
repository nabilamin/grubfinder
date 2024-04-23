import {isLoading} from "../../../../store";
export async function load({params}) {
    try {
        isLoading.set(true);
        const response = await fetch(`https://api.grubfinder.io/session/${params.slug}`,
        {
            method: 'GET',
            headers: {
                'Authorization': '',
                'Content-Type': 'application/json'
            },
        });

        if (response.ok)
            console.log(`Session created successfully with id: ${params.slug}`);
        else
            console.log('Error: Session creation failed');

        const responseBody = await response.json();

        const voteCount = responseBody.vote_count;

        if (voteCount) {
            isLoading.set(false);
            return voteCount;
        }
    }
    catch (error) {
        console.error('Error:', error);
    }
}