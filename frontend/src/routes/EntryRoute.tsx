import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

type RouteParams = {
  key: string;
};

type EntryModel = {
  key: string;
  term: string;
  definitions: string[];
};

export default function EntryRoute() {
  const { key } = useParams<RouteParams>();
  const [loading, setLoading] = useState(false);
  const [entry, setEntry] = useState<EntryModel>();

  const fetchEntry = async () => {
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:8000/entries/${key}`);
      const entry = await response.json();
      setEntry(entry);
    } catch {
      console.error("Catastrophe!");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEntry();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <>
      <h1>{entry?.term}</h1>
      <ul>
        {entry?.definitions.map((definition, i) => (
          <li key={`def-${i}`}>{definition}</li>
        ))}
      </ul>
    </>
  );
}
