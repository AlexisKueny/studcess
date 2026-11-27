create extension if not exists vector;

create table if not exists chunks(
  id uuid primary key default gen_random_uuid(),
  content text not null,
  content_hash text unique,
  embedding vector not null,
  created_at timestamptz not null default now()
);

create or replace function match_chunks(
  query_embedding vector,
  match_threshold float,
  match_count int default 5
)
returns table (
    id uuid, 
    content text,
    similarity float
)
language sql stable
as $$
    select 
      c.id, 
      c.content, 
      -- <=> is the cosine distance
      1 - (c.embedding <=> query_embedding) as similarity
  from chunks c
  where 1 - (posts.embedding <=> query_embedding) > match_threshold
  order by similarity desc
  limit match_count;
$$;