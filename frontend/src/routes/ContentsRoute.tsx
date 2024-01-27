import { useEffect, useState } from "react";
import _ from "lodash";

type TermModel = {
  key: string;
  term: string;
};

export default function ContentsRoute() {
  const [loading, setLoading] = useState(false);
  const [alpha, setAlpha] = useState<string[]>([]);
  const [terms, setTerms] = useState<TermModel[]>([]);

  const fetchTerms = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/entries");
      const terms = await response.json();
      setAlpha(getAlpha(terms));
      setTerms(terms);
    } catch {
      console.error("Catastrophe!");
    } finally {
      setLoading(false);
    }
  };

  const getAlpha = (terms: TermModel[]): string[] => {
    return _.chain(terms)
      .map((term) => term.key[0])
      .uniq()
      .value();
  };

  useEffect(() => {
    fetchTerms();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <>
      {alpha.map((letter) => (
        <a href={`#${letter}`}>{letter.toUpperCase()}</a>
      ))}

      {alpha.map((letter) => (
        <>
          <a id={letter}></a>
          <h2>{letter.toUpperCase()}</h2>
          <ul>
            {terms
              .filter((term) => term.key.startsWith(letter))
              .map((term) => (
                <li key={term.key}>
                  <a href={`/entries/${term.key}`}>{term.term}</a>
                </li>
              ))}
          </ul>
        </>
      ))}
    </>
  );
}
