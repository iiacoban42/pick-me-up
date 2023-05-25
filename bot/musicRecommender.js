require('json5/lib/register');
const contexts = require('./contexts.json5');

let context = null;
let activity_name = ""

async function askContext(textChannel, context, question) {
    const message = await textChannel.send(question);
    for (let emojiOption in context) {
        await message.react(emojiOption);
    }
}

async function fetchMusic(activity, context) {
    await fetch(`http://127.0.0.1:8000/get-new-track/${activity}/${context}/`)
    .then(response => {
        return response.json()
            }
        ).catch(e => console.log(e));
}

module.exports = function(client, interaction) {
    client.on('messageReactionAdd', async (reaction, user) => {
        if (user.bot) return; // Ignore reactions from bots

        const message = reaction.message;

        if (!message.author.bot) return; // Check if the reaction is on a message sent by a bot
        if (message.channel != interaction.channel) return; // Check if the reaction is in the correct channel

        const emoji = reaction.emoji.name;

        if (!Object.keys(context).includes(emoji)) return; // Check if the emoji is a valid choice

        context = context[emoji];

        if (!Object.keys(context).includes("contexts")) { // Check if we are done specifying the context
            interaction.channel.send(`Context selected ${JSON.stringify(context)}`);
            let context_name = context.name
            await fetchMusic(activity_name, context_name)
            .then(url => {
                interaction.channel.send(`Track URL ${url}`);
            });

            return;
        }else{
            activity_name = context.name
        }
        context = context.contexts; // Narrow down the context further
        askContext(interaction.channel, context, 'Specify the context further:')
    });
    context = contexts;
    askContext(interaction.channel, context, 'Please select the current context:')
}