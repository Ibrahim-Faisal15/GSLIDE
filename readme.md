# GSlider

A productive tool designed for students for generating PowerPoint presentations quickly with the help of Artificial Intelligence, without wasting much of your time.

## API Reference

| Parameter    | Type     | Description                                                 |
| :----------- | :------- | :---------------------------------------------------------- |
| `pexels_api` | `string` | **Required**. Generate Images according to the given prompt |

#### Get item

| Parameter | Type     | Description           |
| :-------- | :------- | :-------------------- |
| `groq`    | `string` | **Required**. LLM api |

| Parameter | Type     | Description                                                     |
| :-------- | :------- | :-------------------------------------------------------------- |
| `pptx`    | `string` | **Required**. for rendring LLM repsonse into PowerPoint slides. |

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GROQ_API_KEY`

`PEXEL_API_KEY`
