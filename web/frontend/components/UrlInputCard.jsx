import { useState } from "react";
import { AlphaCard, TextField, Button } from "@shopify/polaris";
import { useAppQuery, useAuthenticatedFetch } from "../hooks";

export function UrlInputCard() {
  const [url, setUrl] = useState("");
  const fetch = useAuthenticatedFetch();

  const handleUrlChange = (value) => {
    setUrl(value);
  };

  const handleSend = () => {
    fetch('http://localhost:5000/process_url', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
};

  return (
    <AlphaCard sectioned>
      <TextField
        label="URL"
        value={url}
        onChange={handleUrlChange}
        autoComplete="off"
      />
      <Button onClick={handleSend}>Send</Button>
    </AlphaCard>
  );
}