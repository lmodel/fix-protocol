package example;

/* metamodel_version: 1.12.0 */
/* version: FIX.Latest_EP312 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One file of the catalogue: the edition it renders and one or more kinds of FIX Latest's elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixRepository  {

  private String repositoryName;
  private String repositoryVersion;
  private String metadataTitle;
  private String metadataDescription;
  private String metadataCreator;
  private String metadataPublisher;
  private String metadataRights;
  private String metadataFormat;
  private String metadataConformsTo;
  private LocalDate metadataCreated;
  private String metadataSource;
  private List<FixSection> fixSections;
  private List<FixCategory> fixCategories;
  private List<FixDatatype> fixDatatypes;
  private List<FixCodeSet> fixCodeSets;
  private List<FixField> fixFields;
  private List<FixComponent> fixComponents;
  private List<FixGroup> fixGroups;
  private List<FixMessage> fixMessages;


}