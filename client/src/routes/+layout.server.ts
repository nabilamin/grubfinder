export async function load({route, url, params}) {
    return ({
        "url": JSON.stringify(url),
        "route": route,
        "params": params
    });
}